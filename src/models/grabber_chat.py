from tortoise.models import Model
from tortoise import fields


class GrabberChat(Model):
    id = fields.IntField(pk=True)
    chat = fields.ForeignKeyField("models.Chat")
    from_chat = fields.ForeignKeyField("models.Chat", "from_chat")
    last_message = fields.CharField(max_length=255, null=True)
    time = fields.DatetimeField(auto_now_add=True)

    class Meta:
        table = "grabber_chats"
