from django.db import models
from django.conf import settings


class PostingSchedule(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    from_hour = models.TimeField()
    to_hour = models.TimeField()
