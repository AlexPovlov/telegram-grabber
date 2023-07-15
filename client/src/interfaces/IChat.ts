import type { IAccount } from "./IAccount";

export interface IChat {
  id: number;
  title: string;
  chat_id: string;
  account_id: string;
  account?: IAccount
}
