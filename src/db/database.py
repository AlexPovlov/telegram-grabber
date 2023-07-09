from tortoise import Tortoise

from src.conf import DB_CONNECTION_URI


async def init_db():
    await Tortoise.init(
        db_url=DB_CONNECTION_URI,
        modules={
            "models": [
                "src.models.account",
                "src.models.chat",
                "src.models.grabber_chat",
                "src.models.spam_chat",
                "src.models.user",
            ]
        },
    )
    await Tortoise.generate_schemas()


async def close_db():
    await Tortoise.close_connections()
    # await Tortoise.close_connections_async()
