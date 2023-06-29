from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select

from src.db.database import get_db
from src.models.user import User

from .base_repository import CRUDRepository


class UserRepository(CRUDRepository):
    def __init__(
        self,
        model: User = Depends(lambda: User),
        db: AsyncSession = Depends(get_db),
    ):
        super().__init__(model, db)

    async def get_from_username(self, username):
        query = select(self.model).where(self.model.username == username)
        result = await self.db.execute(query)
        return result.scalars().first()
