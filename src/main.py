from tortoise import Tortoise

from .conf import APP_NAME, APP_DEBUG, ORIGIN_DOMAINS, models

Tortoise.init_models(
    models,
    "models",
)

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from .db.database import close_db, init_db
from .logger.logger import logger
from .routers.account_router import router as account_router
from .routers.login_router import router as login_router
from .routers.chat_router import router as chat_router
from .routers.spam_chat_router import router as spam_chat_router
from .routers.spam_filter_router import router as spam_filter_router
from .routers.grabber_chat_router import router as grabber_chat_router
from .tasks import tasks

app = FastAPI(debug=APP_DEBUG, title=APP_NAME)

app.add_middleware(
    CORSMiddleware,
    allow_origins=ORIGIN_DOMAINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.exception_handler(Exception)
async def exception_handler(request, exc):
    # Запись ошибки в файл
    logger.error(f"An error occurred: {exc}")
    # Возвращение HTTP-ответа с ошибкой
    return exc, 500


@app.on_event("startup")
async def startup():
    # Запуск подключения к базе в tortoise orm
    await init_db()
    # Крон
    await tasks()


@app.on_event("shutdown")
async def shutdown():
    await close_db()


app.include_router(account_router)
app.include_router(login_router)
app.include_router(chat_router)
app.include_router(spam_chat_router)
app.include_router(spam_filter_router)
# app.include_router(grabber_chat_router)
