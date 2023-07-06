from typing import List

from pydantic import BaseModel

class Chat(BaseModel):
    id: int
    # title: str
    # chat_id: str

    class Config:
        orm_mode = True

class ToChats(BaseModel):
    to_chats: List[int]
