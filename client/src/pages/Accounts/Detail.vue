<script setup lang="ts">
import { User, ArrowLeft, ChatLineSquare } from "@element-plus/icons-vue";
import { ref } from "vue";
import { useRoute, useRouter } from "vue-router";
import { useProgress } from "~/composables/useProgress";
import type { IAccount } from "~/interfaces/IAccount";
import * as api from "~/requests/accounts";

const route = useRoute();
const router = useRouter();
const account = ref<IAccount>();

getData();

async function getData() {
  const progress = useProgress();
  progress.emitStart();
  let { data } = await api.chats(Number(route.params.account_id));
  progress.emitEnd(async () => {
    if (route.params.account_id) {
      account.value = data;
    }
  });
}
</script>

<template>
  <div class="account-detail" v-if="account">
    <el-button
      class="mb-3"
      @click="router.push('/')"
      :icon="ArrowLeft"
      size="small"
    >
      Аккаунты
    </el-button>
    <h3 class="account-detail__title">
      <el-icon><User /></el-icon> Аккаунт
      <span class="account-detail__title-phone">{{ account?.phone }}</span>
    </h3>
    <div class="chat-list" v-if="account.chats">
      <h3 class="chat-list__title">Чаты</h3>
      <div class="row">
        <div class="col-12 col-lg-6 mb-4" v-for="item in account.chats">
          <el-card class="chat-list__item" style="height: 100%">
            <template #header>
              <div>
                <el-button
                  type="primary"
                  size="small"
                  @click="router.push(`/spam-chats/${account.id}/${item.id}`)"
                >
                  <el-icon class="mr-1"><ChatLineSquare /></el-icon>
                  Спамлист
                </el-button>
              </div>
            </template>
            <el-text class="chat-list__item-id d-block mb-2">
              <el-text type="primary">ID: </el-text>
              {{ item.chat_id }}
            </el-text>
            <el-text class="chat-list__item-title d-block">
              <el-text type="primary">Название: </el-text>
              {{ item.title }}
            </el-text>
          </el-card>
        </div>
      </div>
    </div>
  </div>
</template>
