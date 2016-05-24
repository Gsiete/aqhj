# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-05-23 20:23
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import redactor.fields


class Migration(migrations.Migration):

    replaces = [('main', '0001_initial'), ('main', '0002_auto_20160403_1435'), ('main', '0003_auto_20160404_0053'), ('main', '0004_auto_20160404_2211'), ('main', '0005_auto_20160425_2143'), ('main', '0006_match_game_in_season'), ('main', '0007_auto_20160517_2351'), ('main', '0008_auto_20160520_0208'), ('main', '0009_auto_20160520_1356'), ('main', '0010_auto_20160521_2150'), ('main', '0011_match_html_video'), ('main', '0012_auto_20160522_1453'), ('main', '0013_auto_20160522_2019'), ('main', '0014_teamseason_position'), ('main', '0015_auto_20160522_2104'), ('main', '0016_season_short_name')]

    initial = True

    dependencies = [
        ('cities', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Match',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('local_time', models.DateTimeField(verbose_name='local time of the match')),
            ],
        ),
        migrations.CreateModel(
            name='Stadium',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('slug', models.SlugField(default='')),
                ('is_domain_team', models.BooleanField(verbose_name='is the main team of the domain')),
                ('stadium', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.Stadium')),
                ('logo', models.ImageField(null=True, upload_to='team/logo/')),
                ('short_name', models.CharField(blank=True, max_length=150, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Tournament',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('slug', models.SlugField(default='')),
                ('logo', models.ImageField(blank=True, null=True, upload_to='tournament/logo/')),
                ('short_name', models.CharField(blank=True, max_length=150, null=True)),
            ],
        ),
        migrations.AddField(
            model_name='match',
            name='stadium',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='main.Stadium'),
        ),
        migrations.AddField(
            model_name='match',
            name='team_a',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='matches_as_a', to='main.Team'),
        ),
        migrations.AddField(
            model_name='match',
            name='team_b',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='matches_as_b', to='main.Team'),
        ),
        migrations.AddField(
            model_name='match',
            name='tournament',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='main.Tournament'),
        ),
        migrations.AlterModelOptions(
            name='match',
            options={'verbose_name_plural': 'matches'},
        ),
        migrations.RenameField(
            model_name='match',
            old_name='local_time',
            new_name='time',
        ),
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
                ('team', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.Team')),
            ],
        ),
        migrations.RemoveField(
            model_name='match',
            name='tournament',
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
            model_name='season',
            name='tournament',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.Tournament'),
        ),
        migrations.AddField(
            model_name='match',
            name='season',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='main.Season'),
        ),
        migrations.AddField(
            model_name='match',
            name='game_in_season',
            field=models.CharField(blank=True, choices=[('fase-de-grupo-partido-1', 'Fase de grupo - Partido 1'), ('fase-de-grupo-partido-2', 'Fase de grupo - Partido 2'), ('fase-de-grupo-partido-3', 'Fase de grupo - Partido 3'), ('ronda-de-16', 'Ronda de 16'), ('cuartos-de-final', 'Cuartos de final'), ('semi-final', 'Semi-final'), ('final', 'Final'), ('fecha-1', 'Fecha 1'), ('fecha-2', 'Fecha 2'), ('fecha-3', 'Fecha 3'), ('fecha-4', 'Fecha 4'), ('fecha-5', 'Fecha 5'), ('fecha-6', 'Fecha 6'), ('fecha-7', 'Fecha 7'), ('fecha-8', 'Fecha 8'), ('fecha-9', 'Fecha 9'), ('fecha-10', 'Fecha 10'), ('fecha-11', 'Fecha 11'), ('fecha-12', 'Fecha 12'), ('fecha-13', 'Fecha 13'), ('fecha-14', 'Fecha 14'), ('fecha-15', 'Fecha 15'), ('fecha-16', 'Fecha 16'), ('fecha-17', 'Fecha 17'), ('fecha-18', 'Fecha 18'), ('fecha-19', 'Fecha 19'), ('fecha-20', 'Fecha 20'), ('fecha-21', 'Fecha 21'), ('fecha-22', 'Fecha 22'), ('fecha-23', 'Fecha 23'), ('fecha-24', 'Fecha 24'), ('fecha-25', 'Fecha 25'), ('fecha-26', 'Fecha 26'), ('fecha-27', 'Fecha 27'), ('fecha-28', 'Fecha 28'), ('fecha-29', 'Fecha 29'), ('fecha-30', 'Fecha 30'), ('fecha-31', 'Fecha 31'), ('fecha-32', 'Fecha 32'), ('fecha-33', 'Fecha 33'), ('fecha-34', 'Fecha 34'), ('fecha-35', 'Fecha 35'), ('fecha-36', 'Fecha 36'), ('fecha-37', 'Fecha 37'), ('fecha-38', 'Fecha 38'), ('fecha-39', 'Fecha 39')], max_length=30, null=True),
        ),
        migrations.AddField(
            model_name='match',
            name='end_time',
            field=models.DateTimeField(blank=True, null=True, verbose_name='time the match ends'),
        ),
        migrations.AddField(
            model_name='match',
            name='preview_part1',
            field=redactor.fields.RedactorField(blank=True),
        ),
        migrations.AddField(
            model_name='match',
            name='preview_part2',
            field=redactor.fields.RedactorField(blank=True),
        ),
        migrations.AddField(
            model_name='match',
            name='preview_part3',
            field=redactor.fields.RedactorField(blank=True),
        ),
        migrations.AddField(
            model_name='match',
            name='summary',
            field=redactor.fields.RedactorField(blank=True),
        ),
        migrations.AddField(
            model_name='stadium',
            name='short_name',
            field=models.CharField(blank=True, max_length=150, null=True),
        ),
        migrations.AddField(
            model_name='match',
            name='detail_goals_team_a',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='match',
            name='detail_goals_team_b',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='match',
            name='html_video',
            field=models.TextField(blank=True, help_text='&lt;iframe width=&quot;360&quot; height=&quot;203&quot; src=&quot;https://www.youtube.com/embed/CODIGO_DEL_VIDEO&quot; frameborder=&quot;0&quot; allowfullscreen=&quot;&quot;&gt;&lt;/iframe&gt;', null=True),
        ),
        migrations.CreateModel(
            name='TeamGroupStats',
            fields=[
                ('teamseason_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='main.TeamSeason')),
                ('group', models.CharField(max_length=1)),
            ],
            options={
                'abstract': False,
            },
            bases=('main.teamseason',),
        ),
        migrations.AddField(
            model_name='teamseason',
            name='position',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterModelOptions(
            name='teamgroupstats',
            options={'ordering': ['group', 'position']},
        ),
        migrations.AlterModelOptions(
            name='teamseason',
            options={'ordering': ['position']},
        ),
        migrations.AddField(
            model_name='season',
            name='is_main',
            field=models.BooleanField(default=False, verbose_name='indicate that this season is currently the main in the domain'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='season',
            name='short_name',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]