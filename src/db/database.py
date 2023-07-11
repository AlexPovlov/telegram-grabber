from tortoise import Tortoise

from src.conf import DB_CONNECTION_URI, models


async def init_db():
    await Tortoise.init(
        db_url=DB_CONNECTION_URI,
        modules={"models": models},
    )
    await Tortoise.generate_schemas()


async def close_db():
    await Tortoise.close_connections()
    # await Tortoise.close_connections_async()
