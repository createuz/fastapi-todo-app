from uuid import uuid4

from tortoise.models import Model
from tortoise.fields import CharField, UUIDField, BooleanField, DatetimeField


class Todo(Model):
    id = UUIDField(pk=True, default=uuid4)
    title = CharField(max_length=100, null=False)
    done = BooleanField(null=False, default=False)
    created_at = DatetimeField(auto_now_add=True, null=True)

    class Meta:
        table = "todos"
        ordering = ["-created_at"]
