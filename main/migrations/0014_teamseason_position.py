# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-05-22 18:22
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0013_auto_20160522_2019'),
    ]

    operations = [
        migrations.AddField(
            model_name='teamseason',
            name='position',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
