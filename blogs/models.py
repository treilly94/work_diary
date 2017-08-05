from django.db import models
from django.utils import timezone

# blog
class Work_Logs(models.Model):
    author = models.CharField(max_length=250)
    title = models.CharField(max_length=400)
    creation_date = models.DateTimeField('date', default=timezone.now)
    technology = models.CharField(max_length=100)
    type = models.CharField(max_length=1000, default='Work Log')
    description = models.TextField(max_length=1000, default='', blank=True)

    def __str__(self):
        return self.author + " - " + self.title

class Social_Blogs(models.Model):
    author = models.CharField(max_length=250)
    title = models.CharField(max_length=400)
    creation_date = models.DateTimeField('date', default=timezone.now)
    type = models.CharField(max_length=1000, default='Social Blog')
    description = models.TextField(max_length=1000, default='', blank=True)

    def __str__(self):
        return self.author + " - " + self.title

class Technology_Blogs(models.Model):
    author = models.CharField(max_length=250)
    title = models.CharField(max_length=400)
    creation_date = models.DateTimeField('date', default=timezone.now)
    technology = models.CharField(max_length=100)
    type = models.CharField(max_length=1000, default='Technology Blog')
    description = models.TextField(max_length=1000, default='', blank=True)

    def __str__(self):
        return self.author + " - " + self.title