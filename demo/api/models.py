from django.db import models


class Result(models.Model):
    id = models.UUIDField(primary_key=True, editable=False)
    task_id = models.CharField(max_length=255)
    output = models.IntegerField(null=True)
