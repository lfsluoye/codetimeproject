# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2020-04-19 17:17
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('codetime', '0016_auto_20200406_1747'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='template_img_url',
            field=models.CharField(default='', max_length=256),
        ),
        migrations.AlterField(
            model_name='uploadimage',
            name='filename',
            field=models.CharField(default='', max_length=256),
        ),
    ]
