from fastapi import APIRouter, Depends
from src.services.spam_chat_service import SpamChatService

router = APIRouter(prefix="/spam", tags=["Spam Chat"])

@router.delete("/{spam_id}", response_model=bool)
async def delete_spam(
    spam_id: int, service: SpamChatService = Depends(SpamChatService)
):
    await service.delete(spam_id)
    return True


@router.post("/{spam_id}/test", response_model=bool)
async def test_spam(spam_id: int, service: SpamChatService = Depends(SpamChatService)):
    await service.one_send(spam_id)
    return True
