from django.db import models

class Exp(models.Model):
    field = models.CharField(max_length=200)
    description = models.TextField(max_length=500, default='', blank=True)
    date = models.DateTimeField('date')

    def __str__(self):
        return self.field
