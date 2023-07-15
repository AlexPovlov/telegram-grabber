import axios from "axios";
import type { IAccount } from "~/interfaces/IAccount";

export function sendCode(phone: string) {
  return axios.post<boolean>("/api/v1/account/send_code", { phone });
}

export function auth(phone: string, code: string) {
  return axios.post<boolean>("/api/v1/account/auth", { phone, code });
}

export function all() {
  return axios.get<IAccount[]>("/api/v1/account/all");
}
