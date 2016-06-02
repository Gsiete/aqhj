# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-05-30 22:20
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DomainConfig',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_published', models.BooleanField(default=False, verbose_name='indicates weather the Config is published or not')),
                ('domain', models.CharField(choices=[('aquehorajuegaargentina.com', 'aquehorajuegaargentina.com'), ('54.93.126.245:8001', '54.93.126.245:8001')], max_length=60)),
                ('og_locale', models.CharField(blank=True, max_length=8, null=True, verbose_name='Content for the og:locale tag')),
                ('og_site_name', models.CharField(blank=True, max_length=50, null=True, verbose_name='Content for the og:site_name tag')),
                ('facebook_url', models.CharField(blank=True, max_length=150, null=True, verbose_name='facebook url (page, group or whatever)')),
                ('twitter_url', models.CharField(blank=True, max_length=100, null=True, verbose_name='url for the twitter Channel')),
                ('bing_validation_meta', models.CharField(blank=True, max_length=100, null=True, verbose_name='validation code to put into te bing validation meta')),
                ('google_analytics_script', models.TextField(blank=True, null=True)),
            ],
            options={
                'ordering': ['is_published'],
            },
        ),
        migrations.CreateModel(
            name='RouteConfig',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_published', models.BooleanField(default=False, verbose_name='indicates weather the Config is published or not')),
                ('domain', models.CharField(choices=[('aquehorajuegaargentina.com', 'aquehorajuegaargentina.com'), ('54.93.126.245:8001', '54.93.126.245:8001')], max_length=60)),
                ('route', models.CharField(choices=[('index', 'index'), ('match_today', 'match_today'), ('match_before', 'match_before'), ('match_today_no_gis', 'match_today_no_gis'), ('match_before_no_gis', 'match_before_no_gis'), ('past_match', 'past_match'), ('past_match_no_gis', 'past_match_no_gis'), ('last_matches', 'last_matches'), ('group_positions', 'group_positions'), ('nl_success_confirm', 'nl_success_confirm')], max_length=60)),
                ('meta_description', models.TextField(blank=True, null=True, verbose_name='Content for the meta with name="description"')),
                ('title', models.CharField(blank=True, max_length=250, null=True, verbose_name='Content for the head meta title tag(<title>)')),
                ('og_title', models.CharField(blank=True, max_length=250, null=True, verbose_name='Content for the og:title tag')),
                ('og_description', models.TextField(blank=True, null=True, verbose_name='Content for the og:description tag')),
                ('og_type', models.CharField(blank=True, max_length=50, null=True, verbose_name='Content for the og:type tag')),
                ('h1', models.CharField(blank=True, max_length=200, null=True, verbose_name='Content for the main page title (h1)')),
                ('h3', models.CharField(blank=True, max_length=200, null=True, verbose_name='Content for the secondary page title (h3)')),
            ],
            options={
                'ordering': ['is_published'],
            },
        ),
    ]
