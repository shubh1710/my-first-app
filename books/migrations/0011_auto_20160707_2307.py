# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-07-07 17:37
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0010_auto_20160706_1920'),
    ]

    operations = [
        migrations.AlterField(
            model_name='author',
            name='headshot',
            field=models.ImageField(upload_to='/Users/Shubhanker Goyal/mysite/mysite/static/images'),
        ),
    ]
