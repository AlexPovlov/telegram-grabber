from typing import Optional

from fastapi import Depends, HTTPException

from src.libs.tele_sender import Sender
from src.repositories.account_repository import AccountRepository


class AccountService:
    def __init__(self, repo: AccountRepository = Depends(AccountRepository)):
        self.repo = repo

    async def get(self, account_id):
        account = await self.repo.get(account_id)
        if not account:
                raise HTTPException(status_code=404, detail="Account not found")

        return account

    async def send_code(self, phone: str):
        async with Sender(phone) as sender:
            try:
                account = await self.repo.get_from_number(phone)
                if not account:
                    response = await sender.send_code(phone)
                    await self.repo.create({"phone_hash": response.phone_code_hash})
                elif not account.auth:
                    response = await sender.send_code(phone)
                    await self.repo.update(
                        account, {"phone_hash": response.phone_code_hash}
                    )
            except Exception:
                raise HTTPException(status_code=500, detail="Failed send code")

        return True

    async def auth(self, phone: str, code: str, tfa: Optional[str] = None):
        account_db = await self.repo.get_from_number(phone)

        if not account_db:
            raise HTTPException(status_code=404, detail="Account not found")

        if account_db.auth:
            return False

        async with Sender(phone) as sender:
            try:
                await sender.sign_in(account_db.phone, account_db.phone_hash, code, tfa)
                await self.repo.update(account_db, {"auth": True})
            except Exception:
                raise HTTPException(status_code=500, detail="Failed to login")

        return True

    async def accounts(self):
        return await self.repo.get_all()

    async def logout(self, account_id: int):
        account = await self.get(account_id)

        async with Sender(account.phone) as sender:
            try:
                await sender.log_out()
                await self.repo.delete(account)
            except Exception:
                raise HTTPException(status_code=500, detail="Failed to logout")
        return True

    async def get_all_chats(self, account_id: int):
        account = await self.get(account_id)

        async with Sender(account.phone) as sender:
            try:
                chats = await sender.get_chats()

                return chats
            except Exception:
                raise HTTPException(status_code=500, detail="Failed get chats")
