# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-06-23 13:44
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import redactor.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('sites', '0002_alter_domain_unique'),
        ('cities', '0002_country_capital'),
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('is_published', models.BooleanField(default=False)),
                ('priority_in_home', models.IntegerField(blank=True, null=True)),
                ('image_home', models.ImageField(blank=True, null=True, upload_to='article/image/')),
                ('title_short', models.CharField(blank=True, max_length=250, null=True, verbose_name='Short Title (to be shown in home)')),
                ('content_short', redactor.fields.RedactorField(blank=True, null=True, verbose_name='Short Content (to be shown in home)')),
            ],
            options={
                'ordering': ['-created_at'],
            },
        ),
        migrations.CreateModel(
            name='Match',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_published', models.BooleanField(default=False)),
                ('score_team_a', models.IntegerField(blank=True, null=True)),
                ('detail_goals_team_a', models.CharField(blank=True, max_length=100, null=True)),
                ('score_team_b', models.IntegerField(blank=True, null=True)),
                ('detail_goals_team_b', models.CharField(blank=True, max_length=100, null=True)),
                ('game_in_season', models.CharField(blank=True, choices=[('fase-de-grupo-partido-1', 'Fase de grupo - Partido 1'), ('fase-de-grupo-partido-2', 'Fase de grupo - Partido 2'), ('fase-de-grupo-partido-3', 'Fase de grupo - Partido 3'), ('ronda-de-16', 'Ronda de 16'), ('cuartos-de-final', 'Cuartos de final'), ('semi-final', 'Semi-final'), ('final', 'Final'), ('fecha-1', 'Fecha 1'), ('fecha-2', 'Fecha 2'), ('fecha-3', 'Fecha 3'), ('fecha-4', 'Fecha 4'), ('fecha-5', 'Fecha 5'), ('fecha-6', 'Fecha 6'), ('fecha-7', 'Fecha 7'), ('fecha-8', 'Fecha 8'), ('fecha-9', 'Fecha 9'), ('fecha-10', 'Fecha 10'), ('fecha-11', 'Fecha 11'), ('fecha-12', 'Fecha 12'), ('fecha-13', 'Fecha 13'), ('fecha-14', 'Fecha 14'), ('fecha-15', 'Fecha 15'), ('fecha-16', 'Fecha 16'), ('fecha-17', 'Fecha 17'), ('fecha-18', 'Fecha 18'), ('fecha-19', 'Fecha 19'), ('fecha-20', 'Fecha 20'), ('fecha-21', 'Fecha 21'), ('fecha-22', 'Fecha 22'), ('fecha-23', 'Fecha 23'), ('fecha-24', 'Fecha 24'), ('fecha-25', 'Fecha 25'), ('fecha-26', 'Fecha 26'), ('fecha-27', 'Fecha 27'), ('fecha-28', 'Fecha 28'), ('fecha-29', 'Fecha 29'), ('fecha-30', 'Fecha 30'), ('fecha-31', 'Fecha 31'), ('fecha-32', 'Fecha 32'), ('fecha-33', 'Fecha 33'), ('fecha-34', 'Fecha 34'), ('fecha-35', 'Fecha 35'), ('fecha-36', 'Fecha 36'), ('fecha-37', 'Fecha 37'), ('fecha-38', 'Fecha 38'), ('fecha-39', 'Fecha 39')], max_length=30, null=True)),
                ('time', models.DateTimeField(verbose_name='local time of the match')),
                ('end_time', models.DateTimeField(verbose_name='time the match ends')),
                ('og_image', models.ImageField(blank=True, null=True, upload_to='season/og/')),
                ('html_video', models.TextField(blank=True, help_text='&lt;iframe width=&quot;360&quot; height=&quot;203&quot; src=&quot;https://www.youtube.com/embed/CODIGO_DEL_VIDEO&quot; frameborder=&quot;0&quot; allowfullscreen=&quot;&quot;&gt;&lt;/iframe&gt;', null=True)),
            ],
            options={
                'ordering': ['-time'],
                'verbose_name_plural': 'matches',
            },
        ),
        migrations.CreateModel(
            name='Season',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('short_name', models.CharField(blank=True, max_length=50, null=True)),
                ('slug', models.SlugField(default='')),
                ('start', models.DateTimeField(verbose_name='start of the tournament')),
                ('end', models.DateTimeField(verbose_name='end of the tournament')),
                ('is_main', models.BooleanField(verbose_name='indicate that this season is currently the main in the domain')),
                ('groups_og_image', models.ImageField(blank=True, null=True, upload_to='season/groups_og/')),
                ('results_image', models.ImageField(blank=True, null=True, upload_to='season/results/', verbose_name='Results OG image')),
            ],
        ),
        migrations.CreateModel(
            name='Stadium',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('short_name', models.CharField(blank=True, max_length=150, null=True)),
                ('city', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cities.City')),
            ],
        ),
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('short_name', models.CharField(blank=True, max_length=150, null=True)),
                ('slug', models.SlugField(default='')),
                ('logo', models.ImageField(null=True, upload_to='team/logo/')),
                ('is_domain_team', models.BooleanField(verbose_name='is the main team of the domain')),
                ('site', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='sites.Site')),
                ('stadium', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.Stadium')),
            ],
        ),
        migrations.CreateModel(
            name='TeamSeason',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('wins', models.IntegerField(blank=True, null=True)),
                ('draws', models.IntegerField(blank=True, null=True)),
                ('losses', models.IntegerField(blank=True, null=True)),
                ('goals_for', models.IntegerField(blank=True, null=True)),
                ('goals_against', models.IntegerField(blank=True, null=True)),
                ('position', models.IntegerField(blank=True, null=True)),
                ('season', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.Season')),
                ('team', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.Team')),
            ],
            options={
                'ordering': ['position'],
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='TeamSeasonGroup',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('wins', models.IntegerField(blank=True, null=True)),
                ('draws', models.IntegerField(blank=True, null=True)),
                ('losses', models.IntegerField(blank=True, null=True)),
                ('goals_for', models.IntegerField(blank=True, null=True)),
                ('goals_against', models.IntegerField(blank=True, null=True)),
                ('position', models.IntegerField(blank=True, null=True)),
                ('group', models.CharField(max_length=1)),
                ('season', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.Season')),
                ('team', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.Team')),
            ],
            options={
                'ordering': ['group', 'position'],
            },
        ),
        migrations.CreateModel(
            name='Tournament',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('short_name', models.CharField(blank=True, max_length=150, null=True)),
                ('slug', models.SlugField(default='')),
                ('logo', models.ImageField(blank=True, null=True, upload_to='tournament/logo/')),
            ],
        ),
        migrations.CreateModel(
            name='LinkArticle',
            fields=[
                ('article_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='main.Article')),
                ('link', models.CharField(blank=True, max_length=250, null=True)),
            ],
            bases=('main.article',),
        ),
        migrations.CreateModel(
            name='Summary',
            fields=[
                ('article_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='main.Article')),
                ('title', models.CharField(blank=True, max_length=250, null=True)),
                ('sub_title', models.CharField(blank=True, max_length=350, null=True)),
                ('content', redactor.fields.RedactorField(blank=True)),
            ],
            bases=('main.article',),
        ),
        migrations.CreateModel(
            name='ThreeArticles',
            fields=[
                ('article_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='main.Article')),
                ('preview_part1', redactor.fields.RedactorField(blank=True)),
                ('preview_part2', redactor.fields.RedactorField(blank=True)),
                ('preview_part3', redactor.fields.RedactorField(blank=True)),
            ],
            bases=('main.article',),
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
            model_name='article',
            name='match',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.Match'),
        ),
        migrations.AddField(
            model_name='article',
            name='site',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='sites.Site'),
        ),
    ]
