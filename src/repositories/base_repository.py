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
        return await self.model.filter(id=item_id).first()

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

    async def upsert(self, data: dict, key: str, *args, **kwargs):
        unique_fields = [item[key] for item in data]

        existing_models = await self.model.filter(
            *args, **kwargs, **{f"{key}__in": unique_fields}
        ).all()

        existing_models_dict = {getattr(model, key): model for model in existing_models}

        models_to_create = []
        models_to_update = []

        for item in data:
            unique_field = item[key]
            fields = item.keys()
            if unique_field in existing_models_dict:
                model = existing_models_dict[unique_field]
                model.update_from_dict(item)
                models_to_update.append(model)
            else:
                model = self.model(**item)
                models_to_create.append(model)

        if models_to_create:
            await self.model.bulk_create(models_to_create)

        if models_to_update:
            await self.model.bulk_update(models_to_update, fields=fields)

    async def upsert_and_delete(self, entries: dict, key: str, *args, **kwargs):
        unique_fields = [item[key] for item in entries]
        await self.delete_filter(*args, **kwargs, **{f"{key}_not_in": unique_fields})
        await self.upsert(entries, key)
