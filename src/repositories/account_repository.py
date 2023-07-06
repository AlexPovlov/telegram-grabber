from fastapi import Depends

# from src.db.database import get_db
from src.models.account import Account

# from src.models.chat import Chat

from .base_repository import CRUDRepository

# from .chat_repository import ChatRepository


class AccountRepository(CRUDRepository):
    def __init__(
        self,
        model: Account = Depends(lambda: Account),
    ):
        super().__init__(model)

    async def get_from_number(self, phone):
        return await self.model.filter(phone=phone).first()

    async def create_many_chats(self, account_id, chats):
        chat_data = []

        for chat in chats:
            chat_data[str(chat.id)] = {
                "account_id": account_id,
                "title": chat.title,
                "chat_id": str(chat.id),
            }

        chat_repo = ChatRepository(Chat, self.db)
        await chat_repo.upsert_and_delete(chat_data, "chat_id", account_id=account_id)

        return chat_data
