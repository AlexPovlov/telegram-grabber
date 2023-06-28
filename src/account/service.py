from fastapi import Depends
from .repository import AccountRepository
from src.tele_sender import Sender
from typing import Optional
from fastapi import HTTPException


class AccountService:
    def __init__(self, repo: AccountRepository = Depends(AccountRepository)):
        self.repo = repo

    async def send_code(self, phone: str):
        async with Sender(phone) as sender:
            try:
                response = await sender.send_code(phone)
                await self.repo.first_or_create(
                    {"phone": phone},
                    {"phone_hash": response.phone_code_hash},
                )
            except:
                return False
        return True

    async def auth(self, phone: str, code: str, tfa: Optional[str] = None):
        account_db = await self.repo.get_from_number(phone)

        if not account_db:
            raise HTTPException(status_code=404, detail="Account not found")

        async with Sender(phone) as sender:
            try:
                response = await sender.sign_in(
                    account_db.phone, account_db.phone_hash, code, tfa
                )
                await self.repo.update(account_db, {"auth": True})
            except:
                raise HTTPException(status_code=500, detail="Failed to login")
        return True

    async def accounts(self):
        return await self.repo.get_all()

    async def logout(self, account_id: int):
        account = await self.repo.get(account_id)

        if not account:
            raise HTTPException(status_code=404, detail="Account not found")

        async with Sender(account.phone) as sender:
            try:
                await sender.log_out()
            except:
                raise HTTPException(status_code=500, detail="Failed to logout")
        return True
