from celery import Celery
from celery.schedules import crontab
from src.db.database import init_db, close_db
from .conf import APP_NAME, REDIS_CONNECTION
app = Celery('221', broker='redis://localhost:6379/1')

@app.on_after_configure.connect
async def setup_periodic_tasks(sender, **kwargs):
    await init_db()  # Инициализация подключения к базе данных

    sender.add_periodic_task(
        crontab(),  # Каждый день в полночь
        ehe.s("q"),  # Вызывается задача send_email_task с аргументом email
        name='qwe'
    )

# @app.on_cleanup.connect
# async def cleanup_tasks(sender, **kwargs):
#     await close_db()  # Закрытие подключения к базе данных


@app.task
async def ehe(q):
    print(12323123)
