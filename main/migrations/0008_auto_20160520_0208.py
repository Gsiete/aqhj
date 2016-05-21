# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-05-20 00:08
from __future__ import unicode_literals

from django.db import migrations, models
import redactor.fields


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0007_auto_20160517_2351'),
    ]

    operations = [
        migrations.AddField(
            model_name='stadium',
            name='short_name',
            field=models.CharField(blank=True, max_length=150, null=True),
        ),
        migrations.AddField(
            model_name='team',
            name='short_name',
            field=models.CharField(blank=True, max_length=150, null=True),
        ),
        migrations.AddField(
            model_name='tournament',
            name='short_name',
            field=models.CharField(blank=True, max_length=150, null=True),
        ),
        migrations.AlterField(
            model_name='match',
            name='end_time',
            field=models.DateTimeField(blank=True, null=True, verbose_name='time the match ends'),
        ),
        migrations.AlterField(
            model_name='match',
            name='preview_part1',
            field=redactor.fields.RedactorField(blank=True),
        ),
        migrations.AlterField(
            model_name='match',
            name='preview_part2',
            field=redactor.fields.RedactorField(blank=True),
        ),
        migrations.AlterField(
            model_name='match',
            name='preview_part3',
            field=redactor.fields.RedactorField(blank=True),
        ),
        migrations.AlterField(
            model_name='match',
            name='summary',
            field=redactor.fields.RedactorField(blank=True),
        ),
    ]
