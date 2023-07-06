from typing import Optional, List
from .chat_schemas import Chat
from pydantic import BaseModel
from tortoise.contrib.pydantic import pydantic_model_creator, pydantic_queryset_creator

from src.models.account import Account
class CodeRequest(BaseModel):
    phone: str


class AuthRequest(BaseModel):
    phone: str
    code: str
    tfa: Optional[str]


class AccountResponse(BaseModel):
    id: int
    name: Optional[str]
    phone: str

    class Config:
        orm_mode = True

# class AccountSingleResponse(BaseModel):
#     id: int
#     name: Optional[str]
#     phone: str
#     chats: List[Chat] = []

#     class Config:
#         orm_mode = True

AccountSingleResponse = pydantic_queryset_creator(Account)
