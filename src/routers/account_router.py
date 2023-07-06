from typing import List

from fastapi import APIRouter, Depends
from fastapi.security import OAuth2PasswordBearer

from src.schemas.account_schemas import AccountResponse, AuthRequest, CodeRequest, AccountSingleResponse
from src.services.account_service import AccountService
from src.models.account import Account
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

router = APIRouter(prefix="/account", tags=["Account"])


@router.post("/send_code", response_model=None)
async def send_code(
    # token: Annotated[str, Depends(oauth2_scheme)],
    account: CodeRequest,
    service: AccountService = Depends(AccountService),
):
    await service.send_code(account.phone)
    return True


@router.post("/auth", response_model=None)
async def auth(
    # token: Annotated[str, Depends(oauth2_scheme)],
    account: AuthRequest,
    service: AccountService = Depends(AccountService),
):
    await service.auth(account.phone, account.code, account.tfa)
    return True


@router.get("/all", response_model=List[AccountResponse])
async def accounts(
    # token: Annotated[str, Depends(oauth2_scheme)],
    service: AccountService = Depends(AccountService),
):
    return await service.accounts()


@router.get("/{id}")
async def account(
    id: int,
    # token: Annotated[str, Depends(oauth2_scheme)],
    service: AccountService = Depends(AccountService),
):
    account = Account.filter(id=id).prefetch_related('chats')
    # account = account.prefetch_related('chats')
    # data = await service.account(id, ['chats'])
    # await data.fetch_related('chats')
    # print(f'data {account.chats}')
    print(AccountSingleResponse.schema_json())
    data = await AccountSingleResponse.from_queryset(account)
    print(data.json())
    return data

@router.delete("/{account_id}/logout", response_model=None)
async def logout(
    # token: Annotated[str, Depends(oauth2_scheme)],
    account_id: int,
    service: AccountService = Depends(AccountService),
):
    await service.logout(account_id)
    return True


@router.get("/{account_id}/chats", response_model=None)
async def chats(
    # token: Annotated[str, Depends(oauth2_scheme)],
    account_id: int,
    service: AccountService = Depends(AccountService),
):
    data = await service.get_all_chats(account_id)
    return data
