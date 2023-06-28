from typing import Optional

from pydantic import BaseModel


class CodeRequest(BaseModel):
    phone: str


class AuthRequest(BaseModel):
    phone: str
    code: str
    tfa: Optional[str]


class AccountResponse(BaseModel):
    id: int
    name: Optional[str]
    phone: str

    class Config:
        orm_mode = True
