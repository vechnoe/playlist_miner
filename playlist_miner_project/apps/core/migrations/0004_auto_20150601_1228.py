# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_auto_20150601_0524'),
    ]

    operations = [
        migrations.AlterField(
            model_name='radiostation',
            name='begin_date',
            field=models.DateField(default=datetime.datetime(2015, 5, 25, 12, 28, 12, 787945, tzinfo=utc), null=True, verbose_name='Start date of monitoring', blank=True),
        ),
        migrations.AlterField(
            model_name='radiostation',
            name='end_date',
            field=models.DateField(default=datetime.datetime(2015, 6, 1, 12, 28, 12, 788007, tzinfo=utc), null=True, verbose_name='End date of monitoring', blank=True),
        ),
    ]
