# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-09-19 04:12
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('skaters', '0004_auto_20170919_0411'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='skaters',
            name='id',
        ),
        migrations.AddField(
            model_name='skaters',
            name='primary_key',
            field=models.CharField(default='', max_length=100, primary_key=True, serialize=False),
        ),
    ]
