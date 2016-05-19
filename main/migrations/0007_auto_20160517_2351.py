# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-05-17 21:51
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_match_game_in_season'),
    ]

    operations = [
        migrations.AddField(
            model_name='match',
            name='end_time',
            field=models.DateTimeField(null=True, verbose_name='time the match ends'),
        ),
        migrations.AddField(
            model_name='match',
            name='preview_part1',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='match',
            name='preview_part2',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='match',
            name='preview_part3',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='match',
            name='summary',
            field=models.TextField(blank=True),
        ),
    ]