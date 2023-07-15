from fastapi import Depends

from src.models.user import User

from .base_repository import CRUDRepository


class UserRepository(CRUDRepository):
    def __init__(
        self,
        model: User = Depends(lambda: User),
    ):
        super().__init__(model)

    async def get_from_username(self, username):
        return await self.model.filter(username=username).first()
