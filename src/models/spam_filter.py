from tortoise import fields, models


class SpamFilter(models.Model):
    id = fields.IntField(pk=True)
    text = fields.CharField(max_length=500)

    class Meta:
        table = "spam_filters"