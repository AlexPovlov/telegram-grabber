from fastapi import APIRouter


router = APIRouter("/chat", tags=["Chat"])


@router.post("/all")
async def chats():
    pass
