from tortoise import fields, models


class User(models.Model):
    __tablename__ = "users"
    id = fields.IntField(pk=True)
    username = fields.CharField(max_length=255, null=False)
    email = fields.CharField(max_length=255, null=True)
    password = fields.CharField(max_length=255, null=False)
    disabled = fields.BooleanField(default=False)

    class Meta:
        table = "users"
