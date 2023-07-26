import { createRouter, createWebHistory } from "vue-router";
import { useUserStore } from "~/store/user";

const router = createRouter({
  history: createWebHistory(),
  scrollBehavior() {
    return { top: 0 };
  },

  routes: [
    {
      path: "/auth",
      // @ts-ignore
      component: () => import("~/layouts/Auth.vue"),
      name: "auth",
      children: [
        {
          path: "login",
          // @ts-ignore
          component: () => import("~/pages/Login.vue"),
          name: "login",
        },
      ],
    },
    {
      path: "/",
      // @ts-ignore
      component: () => import("~/layouts/Default.vue"),
      beforeEnter: () => {
        const userStore = useUserStore();
        if (!userStore.isAuthorized()) {
          return { name: "login" };
        }
      },
      children: [
        {
          path: "",
          // @ts-ignore
          component: () => import("~/pages/Accounts/List.vue"),
        },
        {
          path: "detail/:account_id",
          // @ts-ignore
          component: () => import("~/pages/Accounts/Detail.vue"),
        },
        {
          path: "spam-chats/:account_id/:chat_id",
          // @ts-ignore
          component: () => import("~/pages/Accounts/SpamChats.vue"),
        },
      ],
    },
  ],
});
export { router };
