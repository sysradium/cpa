# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2015-12-28 13:45
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0002_auto_20151227_1953'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='order_id',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]
