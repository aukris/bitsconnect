# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('connect', '0011_auto_20160129_1327'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='problemsolved',
            name='reply',
        ),
    ]
