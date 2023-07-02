from fastapi import FastAPI


from .logger.logger import logger
from .routers.account_router import router as account_router
from .routers.login_router import router as login_router
from .routers.chat_router import router as chat_router

app = FastAPI()


@app.exception_handler(Exception)
async def exception_handler(request, exc):
    # Запись ошибки в файл
    logger.error(f"An error occurred: {exc}")
    # Возвращение HTTP-ответа с ошибкой
    return exc, 500


app.include_router(account_router)
app.include_router(login_router)
app.include_router(chat_router)
