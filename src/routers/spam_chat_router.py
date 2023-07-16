import asyncio
from typing import Annotated

from fastapi import APIRouter, Depends

from src.services.spam_chat_service import SpamChatService
from src.untils.auth import oauth2_scheme

router = APIRouter(prefix="/spam", tags=["Spam Chat"])


@router.delete("/{spam_id}", response_model=bool)
async def delete_spam(
    token: Annotated[str, Depends(oauth2_scheme)],
    spam_id: int,
    service: SpamChatService = Depends(SpamChatService),
):
    asyncio.create_task(service.delete(spam_id))
    return True


@router.post("/{spam_id}/test", response_model=bool)
async def test_spam(
    token: Annotated[str, Depends(oauth2_scheme)],
    spam_id: int,
    service: SpamChatService = Depends(SpamChatService),
):
    asyncio.create_task(service.one_send(spam_id))
    return True
