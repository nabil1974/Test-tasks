# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-18 13:47
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('table', '0004_auto_20170218_1007'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cell',
            name='content',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
