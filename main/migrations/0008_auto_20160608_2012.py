# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-06-08 20:12
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0007_team_site'),
    ]

    operations = [
        migrations.AddField(
            model_name='match',
            name='summary_sub_title',
            field=models.CharField(blank=True, max_length=350, null=True),
        ),
        migrations.AddField(
            model_name='match',
            name='summary_title',
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
    ]
