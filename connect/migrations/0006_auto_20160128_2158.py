# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('connect', '0005_auto_20160128_2154'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='event',
            options={'permissions': (('event_add', 'Add events custom'),)},
        ),
    ]
