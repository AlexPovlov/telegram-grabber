from fastapi import Depends

from src.models.grabber_chat import GrabberChat

from .base_repository import CRUDRepository


class GrabberChatRepository(CRUDRepository):
    def __init__(
        self,
        model: GrabberChat = Depends(lambda: GrabberChat),
    ):
        super().__init__(model)
