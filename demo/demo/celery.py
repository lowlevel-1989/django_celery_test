from celery import Celery
from django.conf import settings

import os


PROJECT_SETTINGS = 'demo.settings'

# set the default Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', PROJECT_SETTINGS)

app = Celery('demo', backend=settings.CELERY_BROKER_URL)

# Using a string here means the worker don't have to serialize
# the configuration object to child processes.
# - namespace='CELERY' means all celery-related configuration keys
#   should have a `CELERY_` prefix.
app.config_from_object('django.conf:settings', namespace='CELERY')

# REF: https://docs.celeryproject.org/en/latest/userguide/configuration.html
app.conf.task_acks_late = True
app.conf.worker_prefetch_multiplier = 1
app.conf.worker_concurrency = 1

# Load task modules from all registered Django app configs.
app.autodiscover_tasks()
