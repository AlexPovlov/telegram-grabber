from src.conf import DB_CONNECTION_URI

from tortoise import Tortoise


async def init_db():
    await Tortoise.init(
        db_url=DB_CONNECTION_URI,
        modules={
            "models": [
                "src.models.account",
                "src.models.chat",
                "src.models.grabber_chat",
            ]
        },
    )
    await Tortoise.generate_schemas()


async def close_db():
    await Tortoise.close_connections()
    # await Tortoise.close_connections_async()
