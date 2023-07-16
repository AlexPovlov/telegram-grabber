<script setup lang="ts">
import { Postcard } from "@element-plus/icons-vue";
import { ref } from "vue";
import { useRoute } from "vue-router";
import type { IAccount } from "~/interfaces/IAccount";
import * as api from "~/requests/accounts";

const route = useRoute();
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
    <h3 class="account-detail__title">
      <el-icon><Postcard /></el-icon> Аккаунт
      <span class="account-detail__title-phone">{{ account?.phone }}</span>
    </h3>
  </div>
</template>
