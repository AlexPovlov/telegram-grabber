from tortoise.models import Model
from tortoise import fields


class Chat(Model):
    id = fields.IntField(pk=True)
    title = fields.CharField(max_length=255, null=False)
    chat_id = fields.CharField(max_length=255, null=False)
    account_id = fields.ForeignKeyField("models.Account", "chat")
    # from_chats = fields.BackwardFKRelation()

    class Meta:
        table = "chats"
