from fastapi import Depends

from src.models.spam_chat import SpamChat

from .base_repository import CRUDRepository


class SpamChatRepository(CRUDRepository):
    def __init__(
        self,
        model: SpamChat = Depends(lambda: SpamChat),
    ):
        super().__init__(model)
