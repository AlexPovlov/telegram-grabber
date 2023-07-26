import axios from "axios";
import type { IChat } from "~/interfaces/IChat";

export function createSpam(
  chat_id: number,
  data: { to_chats: number[]; time_send: string }
) {
  return axios.post<IChat>(`/api/v1/chat/${chat_id}/spam`, data);
}

export function get(chat_id: number) {
  return axios.get<IChat>(`/api/v1/chat/${chat_id}/spam`);
}
