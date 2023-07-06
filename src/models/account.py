from tortoise.models import Model
from tortoise import fields


class Account(Model):
    id = fields.IntField(pk=True)
    name = fields.CharField(max_length=255, null=True)
    phone = fields.CharField(max_length=255)
    phone_hash = fields.CharField(max_length=255, null=True)
    auth = fields.BooleanField(default=False)
    state = fields.CharField(max_length=255, null=True)
    # chats = relationship('Chat', back_populates="account")

    class Meta:
        table = "accounts"
