<script setup lang="ts">
import { ThemeType, useThemeStore } from '~/store/theme';
import { ref, watch } from 'vue';
import { Moon, Sunny } from '@element-plus/icons-vue';
const themeStore = useThemeStore();
const currentTheme = themeStore.getTheme();
const switchValue = ref<ThemeType>(currentTheme.value);
watch([switchValue], () => {
  themeStore.setTheme(switchValue.value);
});
</script>

<template>
  <el-switch
    v-model="switchValue"
    inline-prompt
    :active-value="ThemeType.LIGHT"
    :inactive-value="ThemeType.DARK"
    :active-icon="Sunny"
    :inactive-icon="Moon"
    style="--el-switch-on-color: #008000"
  />
</template>