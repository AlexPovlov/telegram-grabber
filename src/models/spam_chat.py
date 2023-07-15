from tortoise import fields, models


class SpamChat(models.Model):
    id = fields.IntField(pk=True)
    to_chats = fields.ManyToManyField(
        model_name="models.Chat",
        related_name="to_spam_chats",
        through="spam_to_chats",
        backward_key="spam_chat_id",
        forward_key="to_chat_id"
    )
    chat = fields.ForeignKeyField("models.Chat", "spam_chats")
    message = fields.CharField(max_length=255, null=True)
    time = fields.TimeField(null=True)

    class Meta:
        table = "spam_chats"


class SpamToChat(models.Model):
    id = fields.IntField(pk=True)
    to_chat = fields.ForeignKeyField("models.Chat", related_name="spam_to_chats")
    spam_chat = fields.ForeignKeyField("models.SpamChat", "spam_chat")

    class Meta:
        table = "spam_to_chats"
