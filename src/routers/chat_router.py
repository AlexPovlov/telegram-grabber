from typing import Annotated

from fastapi import APIRouter, Depends

from src.schemas.chat_schemas import (
    ChatFromResponse,
    ChatToResponse,
    FromChatsRequest,
    ToChatsRequest,
)

from src.services.chat_service import ChatService
from src.services.grabber_chat_service import GrabberChatService
from src.services.spam_chat_service import SpamChatService
from src.untils.auth import oauth2_scheme


router = APIRouter(prefix="/chat", tags=["Chat"])


# @router.post("/{chat_id}/grabber", response_model=ChatFromResponse)
# async def set_grabber_chats(
#     chat_id: int,
#     chats: FromChatsRequest,
#     token: Annotated[str, Depends(oauth2_scheme)],
#     service: ChatService = Depends(ChatService),
#     grabber_service: GrabberChatService = Depends(GrabberChatService),
# ):
#     chat = await service.get(chat_id)
#     await grabber_service.set_grabber_chats(chats.from_chats, chat.id)
#     data = await ChatFromResponse.from_tortoise_orm(chat)
#     return data


# @router.get("/{chat_id}/grabber", response_model=ChatFromResponse)
# async def get_grabber_chats(
#     chat_id: int,
#     token: Annotated[str, Depends(oauth2_scheme)],
#     service: ChatService = Depends(ChatService),
# ):
#     chat = await service.get(chat_id)
#     data = await ChatFromResponse.from_tortoise_orm(chat)
#     return data


@router.post("/{chat_id}/spam", response_model=ChatToResponse)
async def set_spam_chats(
    chat_id: int,
    chats: ToChatsRequest,
    token: Annotated[str, Depends(oauth2_scheme)],
    service: ChatService = Depends(ChatService),
    spam_service: SpamChatService = Depends(SpamChatService),
):
    chat = await service.get(chat_id)

    to_chats = await service.get_chat_ids(chat.account_id, chats.to_chats)

    if len(to_chats):
        await spam_service.set_spam_chats(to_chats, chat.id, chats.time_send)

    data = await ChatToResponse.from_tortoise_orm(chat)

    return data


@router.get("/{chat_id}/spam", response_model=ChatToResponse)
async def get_spam_chats(
    chat_id: int,
    token: Annotated[str, Depends(oauth2_scheme)],
    service: ChatService = Depends(ChatService),
):
    chat = await service.get(chat_id)
    data = await ChatToResponse.from_tortoise_orm(chat)
    return data
