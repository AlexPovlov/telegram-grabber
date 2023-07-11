from datetime import datetime, timedelta

from fastapi import Depends
from jose import jwt

from src.conf import ACCESS_TOKEN_EXPIRE_MINUTES, ALGORITHM, SECRET_KEY
from src.repositories.user_repository import UserRepository
from src.untils.hash import Hash


class UserService:
    def __init__(self, repo: UserRepository = Depends(UserRepository)):
        self.repo = repo

    async def authenticate_user(self, username: str, password: str):
        user = await self.repo.get_from_username(username)

        if not user:
            return False
        if not Hash.verify_password(password, user.password):
            return False

        return user

    def create_access_token(self, data: dict, expire_minute=None):
        to_encode = data.copy()
        if expire_minute:
            expire = datetime.utcnow() + timedelta(minutes=float(expire_minute))
        else:
            expire = datetime.utcnow() + timedelta(
                minutes=float(ACCESS_TOKEN_EXPIRE_MINUTES)
            )
        to_encode.update({"exp": expire})
        encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)

        return encoded_jwt

    async def create(self, username, password):
        return await self.repo.first_or_create(
            {"username": username}, {"password": Hash.get_password_hash(password)}
        )


    
