# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-07-06 13:41
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0008_auto_20160621_1406'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='users',
            name='password1',
        ),
        migrations.RemoveField(
            model_name='users',
            name='password2',
        ),
    ]