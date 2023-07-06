from tortoise.models import Model
from tortoise import fields


class Account(Model):
    id = fields.IntField(pk=True)
    name = fields.CharField(max_length=255, null=True)
    phone = fields.CharField(max_length=255)
    phone_hash = fields.CharField(max_length=255, null=True)
    auth = fields.BooleanField(default=False)
    state = fields.CharField(max_length=255, null=True)
    chats: fields.ReverseRelation["Chat"]

    class Meta:
        table = "accounts"


from tortoise.models import Model
from tortoise import fields


class Chat(Model):
    id = fields.IntField(pk=True)
    title = fields.CharField(max_length=255, null=False)
    chat_id = fields.CharField(max_length=255, null=False)
    account: fields.ForeignKeyRelation[Account] = fields.ForeignKeyField(
        "models.Account", related_name="chats"
    )

    class Meta:
        table = "chats"
