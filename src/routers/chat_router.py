from fastapi import APIRouter, Depends

from src.schemas.chat_schemas import ToChats, FromChats, ChatSchema
from src.services.chat_service import ChatService

router = APIRouter(prefix="/chat", tags=["Chat"])


@router.post("/{chat_id}/grabber")
async def set_grabber_chats(
    chat_id: int, chats: FromChats, service: ChatService = Depends(ChatService)
):
    # print(chats)
    chat = await service.get(chat_id)
    await service.set_grabber_chats(chats.from_chats, chat.id)
    data = await ChatSchema.from_tortoise_orm(chat)
    print(chat)
    return data
