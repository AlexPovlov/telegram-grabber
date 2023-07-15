<script setup lang="ts">
import ThemeSwitch from '~/components/ThemeSwitch.vue';
import Logo from '~/components/Logo.vue';
import { SwitchButton } from '@element-plus/icons-vue';
import { computed, onBeforeMount, ref } from 'vue';
import { useRoute, useRouter } from 'vue-router';
import { useUserStore } from '~/store/user';
import { useProgress } from '~/composables/useProgress';

const progress = useProgress();

const route = useRoute();
const router = useRouter();
const userStore = useUserStore();
const logoutLoading = ref(false);
const loadingTimeout = 400;

const items = [
  {
    index: '1',
    name: 'Аккаунты',
    path: '/',
  }
];

async function logout() {
  logoutLoading.value = true;
  await userStore.makeLogoutRequest();
  setTimeout(() => {
    router.push('/auth/login');
  }, loadingTimeout);
}

const activeItem = computed(() => {
  return items.find((i) => i.path === route.fullPath)?.index;
});

onBeforeMount(() => {
  progress.init();
});
</script>

<template>
  <div class="navigation">
    <div class="container" style="padding-top: 12px;">
      <el-progress
        class="common-progress"
        :percentage="progress.percentage.value"
        :status="progress.status.value"
        :show-text="false"
        v-show="progress.percentage.value > 0"
        striped
        striped-flow
      />
      <el-menu class="mt-1" :ellipsis="false" :default-active="activeItem" mode="horizontal">
        <Logo class="navigation__logo" />
        <div class="flex-grow-1" />
        <el-menu-item
          :route="{ path: item.path }"
          class="px-0"
          :index="item.index"
          v-for="item in items"
        >
          <router-link :to="item.path"
            ><span class="route-name">{{ item.name }}</span></router-link
          >
        </el-menu-item>

        <div class="navigation-actions align-self-center ml-2">
          <el-tooltip
            class="box-item"
            effect="dark"
            content="Выйти из системы"
            placement="bottom-end"
          >
            <el-button
              :loading="logoutLoading"
              @click="logout"
              class="mr-2"
              round
              text
              :icon="SwitchButton"
            ></el-button>
          </el-tooltip>
          <ThemeSwitch />
        </div>
      </el-menu>
    </div>
  </div>
</template>
