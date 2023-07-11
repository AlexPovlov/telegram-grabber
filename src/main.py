from tortoise import Tortoise
from .conf import models, APP_NAME

Tortoise.init_models(
    models,
    "models",
)

from fastapi import FastAPI

from .db.database import close_db, init_db
from .logger.logger import logger
from .routers.account_router import router as account_router

# from .routers.login_router import router as login_router
from .routers.chat_router import router as chat_router

app = FastAPI(title=APP_NAME)


@app.exception_handler(Exception)
async def exception_handler(request, exc):
    # Запись ошибки в файл
    logger.error(f"An error occurred: {exc}")
    # Возвращение HTTP-ответа с ошибкой
    return exc, 500


@app.on_event("startup")
async def startup():
    await init_db()


@app.on_event("shutdown")
async def shutdown():
    await close_db()


app.include_router(account_router)
# app.include_router(login_router)
app.include_router(chat_router)
