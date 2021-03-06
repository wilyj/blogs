# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-12-05 11:14
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog_mg', '0004_auto_20181205_1852'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='category_name',
            field=models.CharField(max_length=127, unique=True, verbose_name='类名'),
        ),
        migrations.AlterField(
            model_name='tag',
            name='tag_name',
            field=models.CharField(max_length=127, unique=True, verbose_name='标签名'),
        ),
    ]
