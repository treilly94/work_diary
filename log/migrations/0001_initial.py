# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-09-23 21:30
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='WorkLog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=400)),
                ('technology', models.CharField(default='N/A', max_length=100)),
                ('type', models.CharField(max_length=100)),
                ('description', models.TextField(blank=True, default='', max_length=5000)),
                ('link', models.URLField(blank=True, default='')),
                ('creation_date', models.DateTimeField(default=django.utils.timezone.now, verbose_name='creation_date')),
                ('modified_date', models.DateTimeField(default=django.utils.timezone.now, verbose_name='modified_date')),
                ('author', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
