# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-01-24 17:35
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='author',
            name='headshot',
            field=models.ImageField(upload_to='/Users/Shubhanker/mysite'),
        ),
    ]
