from tortoise import Tortoise

from src.conf import DB_HOST,DB_USER,DB_PASSWORD, DB_NAME, models


async def init_db():
    await Tortoise.init(
        db_url=f"postgres://{DB_USER}:{DB_PASSWORD}@{DB_HOST}/{DB_NAME}",
        modules={"models": models},
    )
    await Tortoise.generate_schemas()


async def close_db():
    await Tortoise.close_connections()
    # await Tortoise.close_connections_async()
