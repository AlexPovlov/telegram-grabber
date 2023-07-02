from typing import Annotated

from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from jose import JWTError, jwt

from src.conf import ALGORITHM, SECRET_KEY
from src.schemas.user_schemas import TokenData

from ..repositories.user_repository import UserRepository

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")


async def get_current_user(
    token: Annotated[str, Depends(oauth2_scheme)],
    repo: UserRepository = Depends(UserRepository),
):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )

    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username: str = payload.get("sub")
        if username is None:
            raise credentials_exception
        token_data = TokenData(username=username)

    except JWTError:
        raise credentials_exception

    user = await repo.get_from_username(token_data.username)

    if user is None:
        raise credentials_exception

    return user


def get_current_active_user(user=Depends(get_current_user)):
    if user.disable:
        raise HTTPException(status_code=400, detail="Inactive user")

    return user
