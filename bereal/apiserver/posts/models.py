from django.db import models
from django.conf import settings


class PostingSchedule(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    from_hour = models.TimeField()
    to_hour = models.TimeField()


class Post(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    created_at = models.DateTimeField(null=True)
    updated_at = models.DateTimeField(null=True, auto_now=True)
    frozen_at = models.DateTimeField()
