# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-04-15 22:33
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_auto_20170414_0122'),
    ]

    operations = [
        migrations.AddField(
            model_name='expense',
            name='entry_type',
            field=models.BooleanField(default=True),
        ),
    ]
