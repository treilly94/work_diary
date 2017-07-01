import datetime
from django.db import models
from django.utils import timezone

from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

class Exp(models.Model):
    user = models.CharField(max_length=100)
    field = models.CharField(max_length=200)
    description = models.TextField(max_length=500, default='', blank=True)
    date = models.DateTimeField('date')

    def __str__(self):
        return self.field

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(max_length=500, blank=True)
    location = models.CharField(max_length=30, blank=True)
    birth_date = models.DateField(null=True, blank=True)
    email_confirmed = models.BooleanField(default=False)

@receiver(post_save, sender=User)
def update_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
    instance.profile.save()