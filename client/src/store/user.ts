import axios from "axios";
import { defineStore } from "pinia";
import { ref } from "vue";
import type { IUser } from "~/interfaces/IUser";
import * as api from "~/requests/auth";

export const useUserStore = defineStore("userStore", () => {
  const user = ref<IUser | null>();

  async function makeLoginRequest(username: string, password: string) {
    let { data } = await api.login(username, password);
    axios.defaults.headers.common.Authorization = `Bearer ${data.access_token}`;
    localStorage.setItem("Authorization", `Bearer ${data.access_token}`);
  }

  async function makeLogoutRequest() {}

  async function makeUserDataRequest() {
    try {
      let { data } = await api.user();
      setUser(data);
    } catch (error) {
      clearUser();
      throw error;
    }
  }

  function setUser(data: IUser) {
    user.value = data;
  }

  function clearUser() {
    user.value = null;
    localStorage.removeItem("Authorization");
  }

  async function getUser() {
    return user;
  }

  function isAuthorized() {
    return !!localStorage.getItem("Authorization");
  }

  return {
    getUser,
    makeLoginRequest,
    makeLogoutRequest,
    isAuthorized,
    makeUserDataRequest,
  };
});
