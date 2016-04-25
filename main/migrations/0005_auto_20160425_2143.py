# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-04-25 19:43
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cities', '0001_initial'),
        ('main', '0004_auto_20160404_2211'),
    ]

    operations = [
        migrations.CreateModel(
            name='Season',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('slug', models.SlugField(default='')),
                ('start', models.DateTimeField(verbose_name='start of the tournament')),
                ('end', models.DateTimeField(verbose_name='end of the tournament')),
            ],
        ),
        migrations.CreateModel(
            name='TeamSeason',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('matches_played', models.IntegerField(blank=True, null=True)),
                ('wins', models.IntegerField(blank=True, null=True)),
                ('draws', models.IntegerField(blank=True, null=True)),
                ('losses', models.IntegerField(blank=True, null=True)),
                ('goals_for', models.IntegerField(blank=True, null=True)),
                ('goals_against', models.IntegerField(blank=True, null=True)),
                ('goals_difference', models.IntegerField(blank=True, null=True)),
                ('points', models.IntegerField(blank=True, null=True)),
                ('season', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.Season')),
            ],
        ),
        migrations.RemoveField(
            model_name='match',
            name='tournament',
        ),
        migrations.RemoveField(
            model_name='stadium',
            name='timezone',
        ),
        migrations.RemoveField(
            model_name='tournament',
            name='end_date',
        ),
        migrations.RemoveField(
            model_name='tournament',
            name='start_date',
        ),
        migrations.AddField(
            model_name='match',
            name='score_team_a',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='match',
            name='score_team_b',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='stadium',
            name='city',
            field=models.ForeignKey(default=6024, on_delete=django.db.models.deletion.CASCADE, to='cities.City'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='team',
            name='logo',
            field=models.ImageField(null=True, upload_to='team/logo/'),
        ),
        migrations.AddField(
            model_name='tournament',
            name='logo',
            field=models.ImageField(blank=True, null=True, upload_to='tournament/logo/'),
        ),
        migrations.AddField(
            model_name='teamseason',
            name='team',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.Team'),
        ),
        migrations.AddField(
            model_name='season',
            name='tournament',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.Tournament'),
        ),
        migrations.AddField(
            model_name='match',
            name='season',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='main.Season'),
        ),
    ]
