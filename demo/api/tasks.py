from celery import shared_task
from .models import Result


@shared_task
def add(pk, x, y):
    result = Result.objects.get(pk=pk)
    result.output = x + y
    result.save()
    return result.output
