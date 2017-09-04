from django.db import models
from django.utils import timezone
from django.core.urlresolvers import reverse

class Exp(models.Model):
    author = models.CharField(max_length=100)
    title = models.CharField(max_length=400)
    technology = models.CharField(max_length=100, default='N/A')
    type = models.CharField(max_length=100)
    description = models.TextField(max_length=500, default='', blank=True)
    link = models.URLField(max_length=200, default='', blank=True)
    creation_date = models.DateTimeField('date', default=timezone.now)

    def get_absolute_url(self):
        return reverse('blog:detail_blog', kwargs={'pk':self.pk})

    def __str__(self):
        return self.title
