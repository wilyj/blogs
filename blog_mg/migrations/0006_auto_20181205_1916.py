# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-12-05 11:16
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog_mg', '0005_auto_20181205_1914'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='article',
            name='tag_name',
        ),
        migrations.DeleteModel(
            name='Tag',
        ),
    ]
