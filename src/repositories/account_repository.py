from fastapi import Depends

from src.models.account import Account

from .base_repository import CRUDRepository


class AccountRepository(CRUDRepository):
    def __init__(
        self,
        model: Account = Depends(lambda: Account),
    ):
        super().__init__(model)

    async def get_from_number(self, phone):
        return await self.model.filter(phone=phone).first()

    async def create_many_chats(self, chats, account):



        return chat_data
