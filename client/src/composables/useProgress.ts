import { ref } from "vue";
import { EventHub, Events } from "~/utils/event-hub";

export function useProgress() {
  const percentage = ref(0);
  const status = ref<"success" | "exception" | "warning">("success");

  let progressInterval: any;

  function init() {
    EventHub.addEventListener(Events.SHOW_PROGRESS_LOADER, () => {
      _start();
    });
    EventHub.addEventListener(Events.HIDE_PROGRESS_LOADER, (e) => {
      // @ts-ignore
      _end(e.data._status);
    });
  }

  function emitStart() {
    EventHub.emit(Events.SHOW_PROGRESS_LOADER);
  }

  function emitEnd(onEnd: () => void, _status?: typeof status.value) {
    const _onEnd = () => {
      onEnd();
      EventHub.removeEventListener(Events.END_PROGRESS_LOADING, _onEnd);
    };
    EventHub.emit(Events.HIDE_PROGRESS_LOADER, { _status });
    EventHub.addEventListener(Events.END_PROGRESS_LOADING, _onEnd);
  }

  function _start() {
    status.value = "success";
    progressInterval = setInterval(() => {
      if (percentage.value <= 100) {
        percentage.value += 10;
      } else {
        clearInterval(progressInterval);
      }
    }, 100);
  }

  function _end(_status?: typeof status.value) {
    setTimeout(() => {
      clearInterval(progressInterval);
      percentage.value = 100;
      if (_status) {
        status.value = _status;
      }
      setTimeout(() => {
        percentage.value = 0;
        EventHub.emit(Events.END_PROGRESS_LOADING);
      }, 500);
    }, 300);
  }

  return { init, percentage, status, emitStart, emitEnd };
}
