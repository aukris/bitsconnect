# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('connect', '0022_auto_20160216_0424'),
    ]

    operations = [
        migrations.AddField(
            model_name='missedcall',
            name='time',
            field=models.DateTimeField(default=datetime.datetime(2016, 2, 15, 23, 10, 46, 619594, tzinfo=utc), auto_now_add=True),
            preserve_default=False,
        ),
    ]
