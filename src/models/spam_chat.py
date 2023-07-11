from tortoise import fields, models


class SpamChat(models.Model):
    id = fields.IntField(pk=True)
    chat = fields.ForeignKeyField("models.Chat", "spam_chats")
    to_chats = fields.JSONField()
    message = fields.CharField(max_length=255, null=True)
    time = fields.TimeField(null=True)

    class Meta:
        table = "spam_chats"
