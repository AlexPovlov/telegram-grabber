from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select

from src.models.account import Account
from .base_repository import CRUDRepository
from src.db.database import get_db


class AccountRepository(CRUDRepository):
    def __init__(
        self,
        model: Account = Depends(lambda: Account),
        db: AsyncSession = Depends(get_db),
    ):
        super().__init__(model, db)

    async def get_from_number(self, phone):
        query = select(self.model).where(self.model.phone == phone)
        result = await self.db.execute(query)
        return result.scalars().first()
