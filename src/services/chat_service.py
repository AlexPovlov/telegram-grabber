from fastapi import Depends, HTTPException

from src.repositories.chat_repository import ChatRepository


class ChatService:
    def __init__(self, repo: ChatRepository = Depends(ChatRepository)):
        self.repo = repo

    async def get(self, chat_id):
        chat = await self.repo.get(chat_id)

        if not chat:
            raise HTTPException(status_code=404, detail="Chat not found")

        return chat

    async def save_many_chats(self, chats, account_id):
        chat_data = [
            {"title": chat.title, "chat_id": str(chat.id), "account_id": account_id}
            for chat in chats
        ]
        await self.repo.upsert_and_delete(chat_data, "chat_id", account_id=account_id)

        return chat_data

    async def get_chat_ids(self, chat_ids, account_id):
        chats = await self.repo.get_all(chat_id__in=chat_ids, account_id=account_id)
        
        return [chat.chat_id for chat in chats]
