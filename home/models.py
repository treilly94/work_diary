from django.core.urlresolvers import reverse
from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
import datetime

class Account(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    creation_date = models.DateTimeField('creation_date', default=timezone.now)
    modified_date = models.DateTimeField('modified_date', default=timezone.now)
    date_of_birth = models.DateTimeField('date_of_birth', default=datetime.datetime.today())
    location = models.CharField(max_length=100)

    def get_absolute_url(self):
        return reverse('home:index')