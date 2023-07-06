from typing import TypeVar


from tortoise.models import Model

# from src.db.database import get_db

# Определим обобщенный тип для моделей
ModelType = TypeVar("ModelType")


class CRUDRepository:
    def __init__(
        self,
        model: Model,
    ):
        self.model = model

    async def get_all(self, *args, **kwargs):
        return await self.model.filter(*args, **kwargs).all()

    async def create(self, item_data: dict) -> ModelType:
        return await self.model.create(**item_data)

    async def get(self, item_id: int, *args, **kwargs) -> ModelType:
        return await self.model.filter(*args, **kwargs).get(id=item_id)

    async def update(self, item: Model, item_data: dict) -> ModelType:
        item = item.update_from_dict(item_data)
        await item.save()
        return item

    async def delete(self, item: Model):
        await item.delete()

    async def delete_filter(self, *args, **kwargs):
        await self.model.filter(*args, **kwargs).delete()

    async def first_or_create(self, item_search: dict, item_data: dict) -> ModelType:
        return await self.model.update_or_create(item_data, **item_search)

    # async def upsert_data(self, entries: dict, key, **kwrds):
    #     entries_to_insert = []
    #     entries = entries.copy()
    #     # get all entries to be updated
    #     s_query = (
    #         select(self.model)
    #         .filter(getattr(self.model, key).in_(entries.keys()))
    #         .filter_by(**kwrds)
    #     )

    #     result = await self.db.execute(s_query)
    #     items = result.scalars().all()

    #     for each in items:
    #         entry = entries.pop(str(getattr(each, key)))
    #         await self.update(each, entry)

    #     # get all entries to be inserted
    #     for entry in entries.values():
    #         entries_to_insert.append(entry)

    #     if entries_to_insert:
    #         i_query = insert(self.model).values(entries_to_insert)
    #         await self.db.execute(i_query)

    #     await self.db.commit()

    # async def upsert_and_delete(self, entries: dict, key, *args, **kwrds):
    #     await self.delete_filter(getattr(self.model, key).not_in(entries.keys()))
    #     await self.upsert_data(entries, key, **kwrds)
