# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-11-20 15:47
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_auto_20191120_1541'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='picture',
            field=models.ImageField(blank=True, upload_to='pictures'),
        ),
    ]