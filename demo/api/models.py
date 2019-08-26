import uuid
from django.db import models


class Result(models.Model):
    id = models.UUIDField(
            primary_key=True,
            default=uuid.uuid4,
            editable=False,
    )
    task_id = models.CharField(max_length=255)
    output = models.IntegerField(null=True) # -1 no action
