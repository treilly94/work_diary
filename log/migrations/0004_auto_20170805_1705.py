# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-08-05 16:05
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('log', '0003_auto_20170703_1850'),
    ]

    operations = [
        migrations.AlterField(
            model_name='exp',
            name='link',
            field=models.URLField(blank=True, default=''),
        ),
    ]