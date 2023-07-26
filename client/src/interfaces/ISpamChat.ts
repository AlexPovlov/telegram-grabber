import type { IChat } from "./IChat"

export interface ISpamChat {
    id: number
    message?: string
    time?: string
    to_chats: IChat[]
}