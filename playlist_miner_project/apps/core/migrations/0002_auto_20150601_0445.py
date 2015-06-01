# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='radiostation',
            name='begin_date',
            field=models.DateTimeField(null=True, verbose_name='Start date of monitoring period', blank=True),
        ),
        migrations.AddField(
            model_name='radiostation',
            name='end_date',
            field=models.DateTimeField(null=True, verbose_name='End date of monitoring period', blank=True),
        ),
    ]
