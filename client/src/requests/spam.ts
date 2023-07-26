import axios from "axios";
import type { IChat } from "~/interfaces/IChat";

export function testSpam(spam_id: number) {
  return axios.post<boolean>(`/api/v1/spam/${spam_id}/test`);
}

export function deleteSpam(spam_id: number) {
  return axios.delete<boolean>(`/api/v1/spam/${spam_id}`);
}
