import datetime
from typing import List

from pydantic import BaseModel
from tortoise.contrib.pydantic import pydantic_model_creator

from src.models.chat import Chat

from .grabber_chat_schemas import GrabberChatSchema
from .spam_chat_schemas import SpamChatSchema


class ToChatsRequest(BaseModel):
    account_id: int
    to_chats: List[str]
    time_send: datetime.time


class FromChatsRequest(BaseModel):
    from_chats: List[int]


ChatSchema = pydantic_model_creator(
    Chat,
    include=(
        "id",
        "title",
        "chat_id",
    ),
)


class ChatFromResponse(ChatSchema):
    grabber_chats: List[GrabberChatSchema]


class ChatToResponse(ChatSchema):
    spam_chats: List[SpamChatSchema]
