# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-06-24 12:40
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('codetime', '0010_auto_20180527_1134'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='userId',
        ),
    ]