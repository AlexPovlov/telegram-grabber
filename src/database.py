from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import sessionmaker

from .conf import DB_CONNECTION_URI

engine = create_async_engine(DB_CONNECTION_URI, pool_pre_ping=True)
assync_session = sessionmaker(autocommit=False, autoflush=False,
                              bind=engine, class_=AsyncSession)


async def get_db() -> AsyncSession:
    async with assync_session() as session:
        yield session
