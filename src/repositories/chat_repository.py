from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession

from src.db.database import get_db
from src.models.chat import Chat

from .base_repository import CRUDRepository


class ChatRepository(CRUDRepository):
    def __init__(
        self,
        model: Chat = Depends(lambda: Chat),
        db: AsyncSession = Depends(get_db),
    ):
        super().__init__(model, db)
