from typing import List

from pydantic import BaseModel


class ToChats(BaseModel):
    to_chats: List[int]
