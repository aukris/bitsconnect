# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('connect', '0013_auto_20160129_1436'),
    ]

    operations = [
        migrations.AddField(
            model_name='problem',
            name='created',
            field=models.DateTimeField(default=datetime.datetime(2016, 1, 29, 9, 43, 5, 155993, tzinfo=utc), auto_now_add=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='problemsolved',
            name='posted_on',
            field=models.DateTimeField(default=datetime.datetime(2016, 1, 29, 9, 43, 8, 715965, tzinfo=utc)),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='problemsolved',
            name='solved_on',
            field=models.DateTimeField(default=datetime.datetime(2016, 1, 29, 9, 43, 14, 91780, tzinfo=utc), auto_now_add=True),
            preserve_default=False,
        ),
    ]
