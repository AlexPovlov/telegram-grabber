from fastapi import Depends, HTTPException

from src.repositories.spam_chat_repository import SpamChatRepository


class SpamChatService:
    def __init__(self, repo: SpamChatRepository = Depends(SpamChatRepository)):
        self.repo = repo

    async def set_spam_chats(self, chat_ids: set, chat_id: int, time):
        await self.repo.create({"chat_id": chat_id, "to_chats": chat_ids, "time": time})

    async def delete(self, spam_id):
        spam = await self.repo.get(spam_id)

        if not spam:
            raise HTTPException(status_code=404, detail="Spam not found")
        
        await self.repo.delete(spam)

    async def send(self):
        pass
