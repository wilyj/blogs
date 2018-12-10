# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-12-05 10:52
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog_mg', '0003_remove_user_user_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='isDelete',
            field=models.BooleanField(default=0),
        ),
        migrations.AlterField(
            model_name='article',
            name='tag_name',
            field=models.ManyToManyField(null=True, to='blog_mg.Tag', verbose_name='标签'),
        ),
    ]