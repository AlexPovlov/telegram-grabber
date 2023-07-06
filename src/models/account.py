from tortoise.models import Model
from tortoise import fields
from .chat import Chat

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
