# from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine, async_sessionmaker
# from sqlalchemy.orm import declarative_base

from src.conf import DB_CONNECTION_URI

# engine = create_async_engine(DB_CONNECTION_URI, pool_pre_ping=True)
# async_session = async_sessionmaker(engine, expire_on_commit=False)


# async def get_db() -> AsyncSession:
#     async with async_session() as session:
#         yield session


# Base = declarative_base()

from tortoise import Tortoise


async def init_db():
    await Tortoise.init(
        db_url=DB_CONNECTION_URI,
        modules={"models": ["src.models.account", "src.models.chat"]},
    )
    await Tortoise.generate_schemas()


async def close_db():
    await Tortoise.close_connections()
    # await Tortoise.close_connections_async()
