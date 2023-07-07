from typing import List
from tortoise.contrib.pydantic import pydantic_model_creator
from pydantic import BaseModel
from src.models.chat import Chat
# class Chat(BaseModel):
#     id: int
#     # title: str
#     # chat_id: str

#     class Config:
#         orm_mode = True

class ToChats(BaseModel):
    to_chats: List[int]

class FromChats(BaseModel):
    from_chats: List[int]


ChatSchema = pydantic_model_creator(Chat, allow_cycles=True)
