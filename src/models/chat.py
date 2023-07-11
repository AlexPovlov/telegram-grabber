from tortoise import fields, models


class Chat(models.Model):
    id = fields.IntField(pk=True)
    title = fields.CharField(max_length=255, null=False)
    chat_id = fields.CharField(max_length=255, null=False)
    account: fields.ForeignKeyRelation["Account"] = fields.ForeignKeyField(
        "models.Account", related_name="chats"
    )

    class Meta:
        table = "chats"
