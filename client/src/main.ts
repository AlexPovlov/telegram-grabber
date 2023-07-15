import '~/boot';
import App from '~/App.vue';
import { createApp } from 'vue';
import { router } from '~/router';
import { createPinia } from 'pinia';
// @ts-ignore
import infiniteScroll from 'vue-infinite-scroll';

const app = createApp(App);

app.use(createPinia());
app.use(router);
app.use(infiniteScroll);
app.mount('#app');
