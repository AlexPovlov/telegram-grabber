from tortoise import Tortoise

Tortoise.init_models(["src.models.account"], "models")
from .db.database import init_db, close_db

from fastapi import FastAPI


from .logger.logger import logger
from .routers.account_router import router as account_router

# from .routers.login_router import router as login_router
# from .routers.chat_router import router as chat_router
from tortoise.contrib.fastapi import register_tortoise


from .conf import DB_CONNECTION_URI

app = FastAPI()


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


# register_tortoise(
#     app,
#     db_url=DB_CONNECTION_URI,
#     modules={"models": ["src.models.account", "src.models.chat", "src.models.grabber_chat"]},
#     generate_schemas=True,
#     add_exception_handlers=True,
# )

app.include_router(account_router)
# app.include_router(login_router)
# app.include_router(chat_router)
