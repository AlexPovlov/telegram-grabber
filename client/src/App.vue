<script setup lang="ts">
import { onBeforeMount, ref } from 'vue';
import { useUserStore } from './store/user';
import UpButton from '~/components/UpButton.vue';
import { useRouter } from 'vue-router';
// @ts-ignore
import ru from 'element-plus/dist/locale/ru';

const locale = ref(ru);
const userStore = useUserStore();
const router = useRouter();

onBeforeMount(async () => {
  try {
    await userStore.makeUserDataRequest();
  } catch (error) {
    if (error === 403) {
      router.push({ path: '/auth/login' });
    }
  }
});
</script>

<template>
  <div>
    <el-config-provider :locale="locale">
      <UpButton />
      <router-view />
    </el-config-provider>
  </div>
</template>
