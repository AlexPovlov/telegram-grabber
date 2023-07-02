from fastapi import APIRouter, Depends

from src.schemas.chat_schemas import ToChats
from src.services.chat_service import ChatService

router = APIRouter(prefix="/chat", tags=["Chat"])


@router.post("/{chat_id}/settochats", response_model=None)
async def set_to_chats(
    chat_id: int, chats: ToChats, service: ChatService = Depends(ChatService)
):
    pass
