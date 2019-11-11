from django.db import models
from .settings import api_settings


class Task(models.Model):
    title = models.CharField(max_length=api_settings.TASK_TITLE_MAX_LENGTH)
    status = models.IntegerField(choices=api_settings.TASK_STATUS_CHOICES)
