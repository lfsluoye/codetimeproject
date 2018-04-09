# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-03-29 15:21
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('codetime', '0002_product'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='knot',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='product',
            name='shipments',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='product',
            name='status',
            field=models.BooleanField(default=False),
        ),
    ]
