<script setup lang="ts">
import { User, ArrowLeft } from "@element-plus/icons-vue";
import { ref } from "vue";
import { useRoute, useRouter } from "vue-router";
import type { IAccount } from "~/interfaces/IAccount";
import * as api from "~/requests/accounts";

const route = useRoute();
const router = useRouter();
const account = ref<IAccount>();

getData();

async function getData() {
  if (route.params.account_id) {
    let { data } = await api.chats(Number(route.params.account_id));
    account.value = data;
  }
}
</script>

<template>
  <div class="account-detail">
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
  </div>
</template>
