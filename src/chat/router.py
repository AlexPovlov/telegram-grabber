from fastapi import APIRouter, Depends


router = APIRouter(
    prefix="/chat",
    tags=["Chat"]
    )


@router.post("/all")
async def chats():
    pass

