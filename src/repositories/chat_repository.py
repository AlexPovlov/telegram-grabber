from fastapi import Depends

from src.models.chat import Chat

from .base_repository import CRUDRepository


class ChatRepository(CRUDRepository):
    def __init__(
        self,
        model: Chat = Depends(lambda: Chat),
    ):
        super().__init__(model)

    async def set_to(self, chat_ids):
        chat = await self.get(1)
        chat2 = await self.get(2)
        print(chat.title)
        chat2.from_chats.extend([chat])
        await self.db.commit()
