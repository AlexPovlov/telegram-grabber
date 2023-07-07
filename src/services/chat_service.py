from fastapi import Depends, HTTPException

from src.repositories.chat_repository import ChatRepository
from src.repositories.grabber_chat_repository import GrabberChatRepository
from src.models.grabber_chat import GrabberChat

class ChatService:
    def __init__(self, repo: ChatRepository = Depends(ChatRepository)):
        self.repo = repo

    async def set_grabber_chats(self, chat_ids: set, chat_id):
        grabber_repo = GrabberChatRepository(GrabberChat)
        data_grabber = [{"chat_id": chat_id, "from_chat_id": id} for id in chat_ids]
        await grabber_repo.upsert(data_grabber, "chat_id")

    async def get(self, chat_id):
        chat = await self.repo.get(chat_id, ["grabbers__from_chat"])

        if not chat:
            raise HTTPException(status_code=404, detail="Chat not found")

        return chat
