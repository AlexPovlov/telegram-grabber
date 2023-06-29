from fastapi import Depends
from datetime import datetime, timedelta
from src.repositories.user_repository import UserRepository
from src.hash import Hash
from jose import JWTError, jwt
from src.conf import ACCESS_TOKEN_EXPIRE_MINUTES, SECRET_KEY, ALGORITHM


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

    def create_access_token(data: dict, expire_minute=None):
        to_encode = data.copy()
        if expire_minute:
            expire = datetime.utcnow() + timedelta(minutes=expire_minute)
        else:
            expire = datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
        to_encode.update({"exp": expire})
        encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
        return encoded_jwt

    # async def get_current_user(token: Annotated[str, Depends(oauth2_scheme)]):
    #     credentials_exception = HTTPException(
    #         status_code=status.HTTP_401_UNAUTHORIZED,
    #         detail="Could not validate credentials",
    #         headers={"WWW-Authenticate": "Bearer"},
    #     )
    #     try:
    #         payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
    #         username: str = payload.get("sub")
    #         if username is None:
    #             raise credentials_exception
    #         token_data = TokenData(username=username)
    #     except JWTError:
    #         raise credentials_exception
    #     user = get_user(fake_users_db, username=token_data.username)
    #     if user is None:
    #         raise credentials_exception
    #     return user

    # async def get_current_active_user(self):
    #     if self.current_user.disabled:
    #         raise HTTPException(status_code=400, detail="Inactive user")
    #     return current_user
