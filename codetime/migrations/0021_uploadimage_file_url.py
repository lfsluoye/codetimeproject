# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2020-04-26 01:45
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('codetime', '0020_product_template_img_md5'),
    ]

    operations = [
        migrations.AddField(
            model_name='uploadimage',
            name='file_url',
            field=models.ImageField(blank=True, default='', max_length=256, upload_to='codetime/upload_images/'),
        ),
    ]