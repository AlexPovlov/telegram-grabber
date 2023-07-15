<script setup lang="ts">
import Navigation from "~/components/Navigation.vue";
</script>

<template>
  <div class="app-layout">
    <navigation />
    <div class="container">
      <h2>Telegram Grabber</h2>
      <router-view />
    </div>
  </div>
</template>

<style lang="scss">
.el-overlay {
  backdrop-filter: blur(4px);
}
</style>
