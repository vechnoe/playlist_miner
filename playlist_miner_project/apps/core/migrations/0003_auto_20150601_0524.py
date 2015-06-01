# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_auto_20150601_0445'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='radiostation',
            name='period',
        ),
        migrations.AlterField(
            model_name='radiostation',
            name='begin_date',
            field=models.DateTimeField(default=datetime.datetime(2015, 5, 25, 5, 24, 17, 948325, tzinfo=utc), null=True, verbose_name='Start date of monitoring', blank=True),
        ),
        migrations.AlterField(
            model_name='radiostation',
            name='end_date',
            field=models.DateTimeField(default=datetime.datetime(2015, 6, 1, 5, 24, 17, 948391, tzinfo=utc), null=True, verbose_name='End date of monitoring', blank=True),
        ),
    ]
