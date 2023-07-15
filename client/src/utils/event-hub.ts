export class HubEvent extends Event {
  public data: any;

  constructor({ type, data }: { type: Events; data: any }) {
    super(type);
    this.data = data;
  }
}

class Hub extends EventTarget {
  private static _instance: Hub;

  public static getInstance(): Hub {
    if (!this._instance) this._instance = new Hub();
    return this._instance;
  }

  public emit(type: Events, data?: any): void {
    this.dispatchEvent(new HubEvent({ type, data }));
  }
}

export const EventHub = Hub.getInstance();

export enum Events {
  SHOW_PROGRESS_LOADER = "SHOW_PROGRESS_LOADER",
  HIDE_PROGRESS_LOADER = "HIDE_PROGRESS_LOADER",
  END_PROGRESS_LOADING = "END_PROGRESS_LOADING",
}
