import datetime
from django.db import models
from django.utils import timezone


class Exp(models.Model):
    user = models.CharField(max_length=100)
    field = models.CharField(max_length=200)
    description = models.TextField(max_length=500, default='', blank=True)
    date = models.DateTimeField('date')

    def __str__(self):
        return self.field
