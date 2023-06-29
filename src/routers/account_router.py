from typing import List
from typing import Annotated
from fastapi import APIRouter, Depends

from src.schemas.account_schemas import AccountResponse, AuthRequest, CodeRequest
from src.services.account_service import AccountService
from fastapi.security import OAuth2PasswordBearer

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

router = APIRouter(prefix="/account", tags=["Account"])


@router.post("/send_code", response_model=None)
async def send_code(
    token: Annotated[str, Depends(oauth2_scheme)],
    account: CodeRequest,
    service: AccountService = Depends(AccountService),
):
    await service.send_code(account.phone)
    return True


@router.post("/auth", response_model=None)
async def auth(account: AuthRequest, service: AccountService = Depends(AccountService)):
    await service.auth(account.phone, account.code, account.tfa)
    return True


@router.get("/all", response_model=List[AccountResponse])
async def accounts(service: AccountService = Depends(AccountService)):
    return await service.accounts()


@router.delete("/logout/{account_id}", response_model=None)
async def logout(account_id: int, service: AccountService = Depends(AccountService)):
    await service.logout(account_id)
    return True
