

from fastapi import Depends, HTTPException

from src.libs.tele_sender import Sender
from src.repositories.chat_repository import ChatRepository


class ChatService:
    def __init__(self, repo: ChatRepository = Depends(ChatRepository)):
        self.repo = repo

    
    


    
