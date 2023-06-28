from fastapi import FastAPI
from .account.router import router as account_router
from .logger import logger

app = FastAPI()

@app.exception_handler(Exception)
async def exception_handler(request, exc):
    # Запись ошибки в файл
    logger.error(f"An error occurred: {exc}")
    # Возвращение HTTP-ответа с ошибкой
    return {"detail": "Internal Server Error"}, 500

app.include_router(account_router)

