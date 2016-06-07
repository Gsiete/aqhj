# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-06-07 06:48
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aqhj_sites', '0004_domainconfig_logo'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='domainconfig',
            name='domain',
        ),
        migrations.RemoveField(
            model_name='routeconfig',
            name='domain',
        ),
        migrations.AddField(
            model_name='domainconfig',
            name='logo_mobile',
            field=models.ImageField(blank=True, null=True, upload_to='site/logo_mobile/'),
        ),
    ]