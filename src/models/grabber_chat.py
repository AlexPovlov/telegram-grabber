from tortoise import fields, models


class GrabberChat(models.Model):
    id = fields.IntField(pk=True)
    chat = fields.ForeignKeyField("models.Chat", "grabber_chats")
    from_chat = fields.OneToOneField("models.Chat", "from_chat")
    last_message = fields.CharField(max_length=255, null=True)
    time = fields.DatetimeField(auto_now_add=True)

    class Meta:
        table = "grabber_chats"
