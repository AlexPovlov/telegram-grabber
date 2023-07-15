import * as env from 'dotenv';
env.config();
import vue from '@vitejs/plugin-vue';
import { defineConfig } from 'vite';
import { resolve } from 'path';
import AutoImport from 'unplugin-auto-import/vite';
import Components from 'unplugin-vue-components/vite';
import { ElementPlusResolver } from 'unplugin-vue-components/resolvers';
import { VitePWA } from 'vite-plugin-pwa'

// https://vitejs.dev/config/
export default defineConfig({
  server: {
    port: Number(process.env.DEV_CLIENT_PORT || 3000),
  },
  resolve: {
    alias: {
      '~': resolve(__dirname, './src'),
    },
  },
  plugins: [
    VitePWA({ registerType: 'autoUpdate' }),
    vue(),
    AutoImport({
      resolvers: [ElementPlusResolver()],
    }),
    Components({
      resolvers: [
        ElementPlusResolver({
          importStyle: 'sass',
        }),
      ],
    }),
  ],
  css: {
    preprocessorOptions: {
      scss: {
        additionalData: `@use "~/scss/element/index.scss" as *;`,
      },
    },
  },
});
