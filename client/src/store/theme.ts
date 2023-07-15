import { defineStore } from 'pinia';
import { ref } from 'vue';

export const useThemeStore = defineStore('themeStore', () => {
  const currentTheme = localStorage.getItem('theme_type') as ThemeType;
  const theme = ref<ThemeType>(currentTheme || ThemeType.DARK);

  setTheme(theme.value);
  
  function getTheme() {
    return theme;
  }

  function setTheme(type: ThemeType) {
    theme.value = type;
    if (theme.value === ThemeType.DARK) {
      document.documentElement.classList.add('dark');
    } else {
      document.documentElement.classList.remove('dark');
    }
    localStorage.setItem('theme_type', type);
  }

  return {
    getTheme,
    setTheme,
  };
});

export enum ThemeType {
  DARK = 'dark',
  LIGHT = 'light',
}
