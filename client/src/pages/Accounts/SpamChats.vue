<script setup lang="ts">
import {
  Plus,
  DArrowLeft,
  ArrowLeft,
  ChatLineSquare,
  Refresh,
  Warning,
  Delete,
} from "@element-plus/icons-vue";
import { ElMessage, ElMessageBox } from "element-plus";

import { computed, ref } from "vue";
import { useRoute, useRouter } from "vue-router";
import { useProgress } from "~/composables/useProgress";
import type { IAccount } from "~/interfaces/IAccount";
import type { IChat } from "~/interfaces/IChat";
import * as apiAccount from "~/requests/accounts";
import * as apiChat from "~/requests/chat";
import * as apiSpam from "~/requests/spam";

const progress = useProgress();
const router = useRouter();
const route = useRoute();
const account = ref<IAccount>();
const chat = ref<IChat>();
const form = ref<{ to_chats: number[]; time_send: string }>({
  to_chats: [],
  time_send: "",
});

getData();

async function getData() {
  progress.emitStart();
  let accountRes = await apiAccount.chats(Number(route.params.account_id));
  let chatRes = await apiChat.get(Number(route.params.chat_id));
  progress.emitEnd(async () => {
    account.value = accountRes.data;
    chat.value = chatRes.data;
  });
}

async function addSpam() {
  if (isValidate.value) {
    await apiChat.createSpam(Number(route.params.chat_id), {
      to_chats: form.value.to_chats,
      time_send: form.value.time_send,
    });
    clearForm();
    getData();
    ElMessage.success("Спам успешно добавлен");
  }
}

async function testSpam(id: number) {
  await ElMessageBox.confirm("Будет запущена рассылка", "Внимание", {
    confirmButtonText: "Продолжить",
    cancelButtonText: "Отмена",
    type: "error",
  });
  progress.emitStart();
  await apiSpam.testSpam(id);
  progress.emitEnd(() => {
    ElMessage.success("Рассылка успешно запущена");

  });
}

async function deleteSpam(id: number) {
  if (id) {
    await ElMessageBox.confirm("Удалить аккаунт?", "Внимание", {
      confirmButtonText: "Подтвердить",
      cancelButtonText: "Отмена",
      type: "error",
    });
    try {
      await apiSpam.deleteSpam(id);
      setTimeout(getData, 1000);
      ElMessage.success("Аккаунт успешно удален");
    } catch (error) {
      ElMessage.warning("Что-то пошло не так");
      console.error(error);
    }
  }
}

function clearForm() {
  form.value = {
    to_chats: [],
    time_send: "",
  };
}

const isValidate = computed(() => form.value.time_send && form.value.to_chats);
</script>

<template>
  <div class="spam-chats" v-if="account && chat">
    <el-button
      class="mb-3"
      @click="router.push('/')"
      :icon="DArrowLeft"
      size="small"
    >
      Аккаунты
    </el-button>
    <el-button
      class="mb-3"
      @click="router.push(`/detail/${account.id}`)"
      :icon="ArrowLeft"
      size="small"
    >
      Аккаунт - {{ account?.phone }}
    </el-button>
    <h3 class="page-title__title">
      <el-icon>
        <el-icon class="mr-1"><ChatLineSquare /></el-icon>
      </el-icon>
      Спамлист
      <span class="page-title__title-info">{{ chat?.title }}</span>
    </h3>
    <h4>Добавить</h4>
    <el-form label-position="top">
      <div class="row">
        <div class="col-12 col-md-8">
          <el-form-item label="Время отправки">
            <el-input
              v-model="form.time_send"
              placeholder="Введите время отправки"
            />
          </el-form-item>
          <el-form-item label="Целевые чаты">
            <el-select
              class="w-100"
              allow-create
              filterable
              v-model="form.to_chats"
              placeholder="Выберите чаты"
              multiple
            >
              <el-option
                v-for="item in account.chats"
                :key="item.id"
                :label="item.title"
                :value="item.id"
              />
            </el-select>
          </el-form-item>
          <div class="d-flex">
            <el-button type="primary" :icon="Plus" @click="addSpam">
              Сохранить
            </el-button>
            <el-button type="warning" :icon="Refresh" @click="clearForm" />
          </div>
        </div>
      </div>
    </el-form>
    <div
      class="common-list__list"
      v-if="chat.spam_chats && chat.spam_chats.length"
    >
      <h3>Добавленные</h3>
      <div class="common-list__list">
        <div class="row">
          <div class="col-12 col-lg-6 mb-4" v-for="item in chat.spam_chats">
            <el-card class="chat-list__item" style="height: 100%">
              <template #header>
                <div>
                  <el-button
                    @click="testSpam(item.id)"
                    size="small"
                    :icon="Warning"
                  >
                    Tестировать
                  </el-button>
                  <el-button
                    @click="deleteSpam(item.id)"
                    size="small"
                    type="warning"
                    :icon="Delete"
                  >
                    Удалить
                  </el-button>
                </div>
              </template>
              <el-text class="chat-list__item-id d-block mb-2">
                <el-text type="primary">Время: </el-text>
                {{ item.time }}
              </el-text>
              <el-text class="chat-list__item-title d-block">
                <el-text type="primary">Чаты: </el-text>
                {{ item.to_chats.map((i) => i.title).join(", ") }}
              </el-text>
            </el-card>
          </div>
        </div>
      </div>
    </div>
    <el-empty v-else description="Нет добавленных" />
  </div>
</template>
