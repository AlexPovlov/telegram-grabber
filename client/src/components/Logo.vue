<script setup lang="ts">
import { ThemeType, useThemeStore } from "~/store/theme";
// @ts-ignore
import logo from "~/public/logo.svg";

const themeStore = useThemeStore();
const currentTheme = themeStore.getTheme();
</script>

<template>
  <div>
    <img class="app-logo" :src="logo" alt="F10" />
  </div>
</template>

<style lang="scss">
.app-logo {
  max-width: 100%;
}
</style>
