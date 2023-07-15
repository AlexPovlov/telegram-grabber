from fastapi import APIRouter, Depends
from src.services.grabber_chat_service import GrabberChatService

router = APIRouter(prefix="/grabber", tags=["Grabber Chat"])

@router.delete("/grabber/{grabber_id}", response_model=bool)
async def delete_grabber(
    spam_id: int, service: GrabberChatService = Depends(GrabberChatService)
):
    await service.delete(spam_id)
    return True
