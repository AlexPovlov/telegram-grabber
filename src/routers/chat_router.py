from fastapi import APIRouter, Depends

from src.schemas.chat_schemas import (ChatFromResponse, ChatToResponse,
                                      FromChatsRequest, ToChatsRequest)
from src.services.account_service import AccountService
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
async def get_grabber_chats(
    chat_id: int,
    service: ChatService = Depends(ChatService),
):
    chat = await service.get(chat_id)
    data = await ChatFromResponse.from_tortoise_orm(chat)
    return data



@router.delete("/grabber/{grabber_id}", response_model=bool)
async def delete_grabber(
    spam_id: int, service: GrabberChatService = Depends(GrabberChatService)
):
    await service.delete(spam_id)
    return True


@router.post("/{chat_id}/spam", response_model=ChatToResponse | None)
async def set_spam_chats(
    chat_id: int,
    chats: ToChatsRequest,
    service: ChatService = Depends(ChatService),
    spam_service: SpamChatService = Depends(SpamChatService),
    account_service: AccountService = Depends(AccountService),
):
    chat = await service.get(chat_id)
    account = await account_service.get(chats.account_id)

    if(chat.account_id != account.id):
        return

    to_chats = await service.get_chat_ids(chats.to_chats, account.id)

    if len(to_chats):
        await spam_service.set_spam_chats(
            to_chats, chat.id, account.id, chats.time_send
        )

    data = await ChatToResponse.from_tortoise_orm(chat)

    return data


@router.get("/{chat_id}/spam", response_model=ChatToResponse)
async def get_spam_chats(
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
async def test_spam(
    spam_id: int, service: SpamChatService = Depends(SpamChatService)
):
    await service.one_send(spam_id)
    return True
