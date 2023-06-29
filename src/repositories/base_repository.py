from typing import TypeVar

from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select

from src.db.database import get_db

# Определим обобщенный тип для моделей
ModelType = TypeVar("ModelType")


class CRUDRepository:
    def __init__(
        self,
        model,
        db: AsyncSession = Depends(get_db),
    ):
        self.model = model
        self.db = db

    async def get_all(self):
        query = select(self.model)
        result = await self.db.execute(query)
        return result.scalars().all()

    async def create(self, item_data: dict) -> ModelType:
        db_item = self.model(**item_data)
        self.db.add(db_item)
        await self.db.commit()
        await self.db.refresh(db_item)
        return db_item

    async def get(self, item_id: int) -> ModelType:
        query = select(self.model).where(self.model.id == item_id)
        result = await self.db.execute(query)
        item = result.scalars().first()
        return item

    async def update(self, item: ModelType, item_data: dict) -> ModelType:
        for key, value in item_data.items():
            setattr(item, key, value)

        await self.db.commit()
        await self.db.refresh(item)
        return item

    async def delete(self, item: ModelType):
        async with self.db.begin():
            self.db.delete(item)
            await self.db.commit()

    async def first_or_create(self, search_params: dict, item_data: dict) -> ModelType:
        query = select(self.model).filter_by(**search_params)
        result = await self.db.execute(query)
        item = result.scalars().first()
        data = search_params | item_data

        if item:
            return await self.update(item, data)

        return await self.create(data)
