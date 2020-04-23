# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2020-04-06 17:42
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('codetime', '0014_product_retention_samples'),
    ]

    operations = [
        migrations.CreateModel(
            name='UploadImage',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('filename', models.CharField(default='', max_length=252)),
                ('file_md5', models.CharField(max_length=128)),
                ('file_type', models.CharField(max_length=32)),
                ('file_size', models.IntegerField()),
                ('created_at', models.DateTimeField(default=datetime.datetime.now)),
                ('update_at', models.DateTimeField(default=datetime.datetime.now)),
            ],
            options={
                'db_table': 'upload_image',
            },
        ),
    ]
