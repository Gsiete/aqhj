# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-06-09 00:15
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import redactor.fields


class Migration(migrations.Migration):

    dependencies = [
        ('sites', '0002_alter_domain_unique'),
        ('main', '0008_auto_20160608_2012'),
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('is_published', models.BooleanField(default=False, verbose_name='indicates weather the Match is published or not')),
            ],
            options={
                'ordering': ['-id'],
            },
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
