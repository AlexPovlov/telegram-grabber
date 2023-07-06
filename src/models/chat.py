from tortoise.models import Model
from tortoise import fields


class Chat(Model):
    id = fields.IntField(pk=True)
    title = fields.CharField(max_length=255, null=False)
    chat_id = fields.CharField(max_length=255, null=False)
    account: fields.ForeignKeyRelation["Account"] = fields.ForeignKeyField("models.Account", related_name='chats')
    # from_chats = fields.BackwardFKRelation()

    class Meta:
        table = "chats"
