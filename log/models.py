from django.db import models
from django.utils import timezone


class Exp(models.Model):
    author = models.CharField(max_length=100)
    title = models.CharField(max_length=400)
    technology = models.CharField(max_length=100, default='N/A')
    type = models.CharField(max_length=100)
    description = models.TextField(max_length=500, default='', blank=True)
    link = models.URLField(max_length=200, default='', blank=True)
    creation_date = models.DateTimeField('date', default=timezone.now)
    likes = models.IntegerField(default=0)
    favourite = models.IntegerField(default=0)
    is_favourite = models.BooleanField(default=False)

    def __str__(self):
        return self.title
