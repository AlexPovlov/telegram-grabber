from fastapi import Depends

from src.models.spam_filter import SpamFilter

from .base_repository import CRUDRepository


class SpamFilterRepository(CRUDRepository):
    def __init__(
        self,
        model: SpamFilter = Depends(lambda: SpamFilter),
    ):
        super().__init__(model)
