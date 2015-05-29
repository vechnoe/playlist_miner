# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Airplay',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('date', models.DateTimeField(null=True, verbose_name='Date of airplay', blank=True)),
            ],
            options={
                'ordering': ['-date'],
                'verbose_name': 'Airplay',
                'verbose_name_plural': 'Airplays',
            },
        ),
        migrations.CreateModel(
            name='Radiostation',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=255, verbose_name='Name')),
                ('url', models.CharField(max_length=255, verbose_name='URL')),
                ('data_url', models.CharField(max_length=500, verbose_name='Data URL')),
                ('period', models.PositiveIntegerField(default=7, verbose_name='Monitoring period (days)')),
            ],
            options={
                'verbose_name': 'Radiostation',
                'verbose_name_plural': 'Radiostations',
            },
        ),
        migrations.CreateModel(
            name='Song',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=255, verbose_name='Song title')),
                ('artist', models.CharField(max_length=255, verbose_name='Artist')),
                ('radiostation', models.ForeignKey(to='core.Radiostation')),
            ],
            options={
                'verbose_name': 'Song',
                'verbose_name_plural': 'Songs',
            },
        ),
        migrations.AddField(
            model_name='airplay',
            name='radiostation',
            field=models.ForeignKey(to='core.Radiostation'),
        ),
        migrations.AddField(
            model_name='airplay',
            name='song',
            field=models.ForeignKey(to='core.Song'),
        ),
    ]
