from typing import List, Optional

from pydantic import BaseModel
from tortoise.contrib.pydantic import pydantic_model_creator

from src.models.account import Account

from .chat_schemas import ChatSchema


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


AccountSchema = pydantic_model_creator(
    Account,
    include=(
        "phone",
        "name",
        "id",
    ),
)


class AccountSingleResponse(AccountSchema):
    chats: List[ChatSchema]
