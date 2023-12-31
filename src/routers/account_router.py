import asyncio
from typing import Annotated, List

from fastapi import APIRouter, Depends

from src.schemas.account_schemas import (
    AccountResponse,
    AccountSingleResponse,
    AuthRequest,
    CodeRequest,
)
from src.services.account_service import AccountService
from src.services.chat_service import ChatService
from src.untils.auth import oauth2_scheme

router = APIRouter(prefix="/account", tags=["Account"])


@router.post("/send_code", response_model=bool)
async def send_code(
    token: Annotated[str, Depends(oauth2_scheme)],
    account: CodeRequest,
    service: AccountService = Depends(AccountService),
):
    asyncio.create_task(service.send_code(account.phone))
    return True


@router.post("/auth", response_model=bool)
async def auth(
    token: Annotated[str, Depends(oauth2_scheme)],
    account: AuthRequest,
    service: AccountService = Depends(AccountService),
):
    asyncio.create_task(service.auth(account.phone, account.code, account.tfa))
    return True


@router.get("/all", response_model=List[AccountResponse])
async def accounts(
    token: Annotated[str, Depends(oauth2_scheme)],
    service: AccountService = Depends(AccountService),
):
    return await service.accounts()


@router.delete("/{account_id}/logout", response_model=bool)
async def logout(
    token: Annotated[str, Depends(oauth2_scheme)],
    account_id: int,
    service: AccountService = Depends(AccountService),
):
    asyncio.create_task(service.logout(account_id))
    return True


@router.get("/{account_id}/chats", response_model=AccountSingleResponse)
async def chats(
    token: Annotated[str, Depends(oauth2_scheme)],
    account_id: int,
    service: AccountService = Depends(AccountService),
    chat_service: ChatService = Depends(ChatService),
):
    account = await service.get(account_id)
    chats = await service.get_all_chats(account_id)
    await chat_service.save_many_chats(chats, account_id)
    data = await AccountSingleResponse.from_tortoise_orm(account)
    return data