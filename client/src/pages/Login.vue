<script setup lang="ts">
import Logo from "~/components/Logo.vue";
import { ElMessage } from "element-plus";
import { reactive, ref } from "vue";
import { ArrowRight } from "@element-plus/icons-vue";
import { useUserStore } from "~/store/user";
import { useRouter } from "vue-router";

const router = useRouter();
const userStore = useUserStore();

const form = reactive({
  username: "",
  password: "",
});

const loading = ref(false);

async function login() {
  try {
    loading.value = true;
    await userStore.makeLoginRequest(form.username, form.password);
    await userStore.makeUserDataRequest();
    router.push("/");
    loading.value = false;
  } catch (error: any) {
    ElMessage.warning("Ошибка авторизации");
    loading.value = false;
  }
}
</script>

<template>
  <div class="login-page">
    <div class="login-page__wrap">
      <div class="login-page__header">
        <h2 class="login-page__header-title">Telegram Grabber</h2>
        <Logo class="login-page__header-logo" />
      </div>
      <el-form class="login-page__form" label-position="top">
        <el-form-item label="Имя пользователя">
          <el-input
            placeholder="Введите имя пользователя..."
            v-model="form.username"
          />
        </el-form-item>
        <el-form-item label="Пароль">
          <el-input
            placeholder="Введите пароль..."
            v-model="form.password"
            type="password"
          />
        </el-form-item>
        <el-button
          type="primary"
          :loading="loading"
          :icon="ArrowRight"
          @click="login"
        >
          Войти</el-button
        >
      </el-form>
    </div>
  </div>
</template>
