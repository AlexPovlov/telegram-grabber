from fastapi import APIRouter, Depends

from src.schemas.chat_schemas import (
    ToChatsRequest,
    FromChatsRequest,
    ChatFromResponse,
    ChatToResponse,
    ChatFromResponse,
)
from src.services.chat_service import ChatService
from src.services.grabber_chat_service import GrabberChatService
from src.services.spam_chat_service import SpamChatService

router = APIRouter(prefix="/chat", tags=["Chat"])


@router.post("/{chat_id}/grabber", response_model=ChatFromResponse)
async def set_grabber_chats(
    chat_id: int,
    chats: FromChatsRequest,
    service: ChatService = Depends(ChatService),
    grabber_service: GrabberChatService = Depends(GrabberChatService),
):
    chat = await service.get(chat_id)
    await grabber_service.set_grabber_chats(chats.from_chats, chat.id)
    data = await ChatFromResponse.from_tortoise_orm(chat)
    return data


@router.get("/{chat_id}/grabber", response_model=ChatFromResponse)
async def set_grabber_chats(
    chat_id: int,
    service: ChatService = Depends(ChatService),
):
    chat = await service.get(chat_id)
    data = await ChatFromResponse.from_tortoise_orm(chat)
    return data


@router.post("/{chat_id}/spam", response_model=ChatToResponse)
async def set_spam_chats(
    chat_id: int,
    chats: ToChatsRequest,
    service: ChatService = Depends(ChatService),
    spam_service: SpamChatService = Depends(SpamChatService),
):
    chat = await service.get(chat_id)
    await spam_service.set_spam_chats(
        chats.to_chats, chat.id, chats.account_id, chats.time_send
    )
    data = await ChatToResponse.from_tortoise_orm(chat)
    return data


@router.get("/{chat_id}/spam", response_model=ChatToResponse)
async def set_spam_chats(
    chat_id: int,
    service: ChatService = Depends(ChatService),
):
    chat = await service.get(chat_id)
    data = await ChatToResponse.from_tortoise_orm(chat)
    return data


@router.delete("/spam/{spam_id}", response_model=bool)
async def delete_spam(
    spam_id: int, service: SpamChatService = Depends(SpamChatService)
):
    await service.delete(spam_id)
    return True


@router.post("/spam/{spam_id}/test", response_model=bool)
async def delete_spam(
    spam_id: int, service: SpamChatService = Depends(SpamChatService)
):
    await service.one_send(spam_id)
    return True


@router.delete("/grabber/{grabber_id}", response_model=bool)
async def delete_spam(
    spam_id: int, service: GrabberChatService = Depends(GrabberChatService)
):
    await service.delete(spam_id)
    return True
