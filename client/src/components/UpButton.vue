<script setup lang="ts">
import { ArrowUp } from '@element-plus/icons-vue';
import { onBeforeMount, ref } from 'vue';
const topY = ref(0);
onBeforeMount(() => {
  document.onscroll = () => {
    topY.value = window.top?.scrollY || 0;
  };
});
function scrollTop() {
  window.scrollTo(0, 0);
}
</script>
<template>
  <el-button
    v-show="topY > 100"
    class="up-button"
    size="large"
    type="primary"
    :icon="ArrowUp"
    @click="scrollTop"
    circle
  />
</template>
