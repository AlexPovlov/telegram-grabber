from typing import TypeVar

from fastapi import Depends
from sqlalchemy import delete, insert, select
from sqlalchemy.ext.asyncio import AsyncSession

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

    async def get_all(self, **kwrds):
        query = select(self.model).filter_by(kwrds)
        result = await self.db.execute(query)
        return result.scalars().all()

    async def create(self, item_data: dict) -> ModelType:
        db_item = self.model(**item_data)
        self.db.add(db_item)
        await self.db.commit()
        await self.db.refresh(db_item)
        return db_item

    async def get(self, item_id: int, **kwrds) -> ModelType:
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

    async def delete_filter(self, *args, **kwrds):
        query = delete(self.model).filter(*args).filter_by(**kwrds)
        await self.db.execute(query)

    async def first_or_create(self, search_params: dict, item_data: dict) -> ModelType:
        query = select(self.model).filter_by(**search_params)
        result = await self.db.execute(query)
        item = result.scalars().first()
        data = search_params | item_data

        if item:
            return await self.update(item, data)

        return await self.create(data)

    async def upsert_data(self, entries: dict, key, **kwrds):
        entries_to_insert = []
        entries = entries.copy()
        # get all entries to be updated
        s_query = (
            select(self.model)
            .filter(getattr(self.model, key).in_(entries.keys()))
            .filter_by(**kwrds)
        )

        result = await self.db.execute(s_query)
        items = result.scalars().all()

        for each in items:
            entry = entries.pop(str(getattr(each, key)))
            await self.update(each, entry)

        # get all entries to be inserted
        for entry in entries.values():
            entries_to_insert.append(entry)

        if entries_to_insert:
            i_query = insert(self.model).values(entries_to_insert)
            await self.db.execute(i_query)

        await self.db.commit()

    async def upsert_and_delete(self, entries: dict, key, *args, **kwrds):
        await self.delete_filter(getattr(self.model, key).not_in(entries.keys()))
        await self.upsert_data(entries, key, **kwrds)
