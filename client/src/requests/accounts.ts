import axios from "axios";
import type { IAccount } from "~/interfaces/IAccount";

export function sendCode(phone: string) {
  return axios.post<boolean>("/api/v1/account/send_code", { phone });
}

export function auth(phone: string, code: string, tfa: string) {
  return axios.post<boolean>("/api/v1/account/auth", { phone, code, tfa });
}

export function all() {
  return axios.get<IAccount[]>("/api/v1/account/all");
}

export function chats(id: number) {
  return axios.get<IAccount>(`/api/v1/account/${id}/chats`);
}

export function logout(id: number) {
  return axios.delete<boolean>(`/api/v1/account/${id}/logout`);
}
