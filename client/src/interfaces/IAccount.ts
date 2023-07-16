import type { IChat } from "./IChat";

export interface IAccount {
  id?: number;
  name?: string;
  phone: string;
  auth: boolean;
  chats?: IChat[];
}
