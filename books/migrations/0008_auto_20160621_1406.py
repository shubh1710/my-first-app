# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-06-21 08:36
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0007_auto_20160621_1404'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='User',
            new_name='Users',
        ),
    ]