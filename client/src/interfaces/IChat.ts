import type { IAccount } from "./IAccount";
import type { ISpamChat } from "./ISpamChat";

export interface IChat {
  id: number;
  title: string;
  chat_id: string;
  account_id: string;
  account?: IAccount,
  spam_chats: ISpamChat[]
}
