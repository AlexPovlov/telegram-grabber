from typing import Annotated

from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm

from src.schemas.user_schemas import Token, User
from src.services.user_service import UserService
from src.untils.auth import get_current_user

router = APIRouter(tags=["Auth"])


@router.post("/create/superuser", response_model=User)
async def create_admin_user(service: UserService = Depends(UserService)):
    return await service.create("adminim", "password")


@router.post("/token", response_model=Token)
async def login_for_access_token(
    form_data: Annotated[OAuth2PasswordRequestForm, Depends()],
    service: UserService = Depends(UserService),
):
    user = await service.authenticate_user(form_data.username, form_data.password)

    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )

    access_token = service.create_access_token({"sub": user.username})
    return {"access_token": access_token, "token_type": "bearer"}


@router.get("/users/me/", response_model=User)
async def read_users_me(current_user: Annotated[User, Depends(get_current_user)]):
    return current_user
