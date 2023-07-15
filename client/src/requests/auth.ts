import axios from "axios";
import type { IUser } from "~/interfaces/IUser";

export function login(username: string, password: string) {
  return axios.post(
    "/api/v1/token",
    { username, password },
    { headers: { "content-type": "application/x-www-form-urlencoded" } }
  );
}

export function user() {
  return axios.get<IUser>("/api/v1/users/me/");
}
