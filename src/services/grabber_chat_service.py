from fastapi import Depends, HTTPException

from src.repositories.grabber_chat_repository import GrabberChatRepository


class GrabberChatService:
    def __init__(self, repo: GrabberChatRepository = Depends(GrabberChatRepository)):
        self.repo = repo

    async def set_grabber_chats(self, chat_ids: set, chat_id):
        data_grabber = [{"chat_id": chat_id, "from_chat_id": id} for id in chat_ids]
        await self.repo.upsert(data_grabber, "chat_id")

    async def delete(self, grabber_id):
        grabber = await self.repo.get(grabber_id)

        if not grabber:
            raise HTTPException(status_code=404, detail="Grabber not found")

        await self.repo.delete(grabber)
