# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('connect', '0026_auto_20160502_2320'),
    ]

    operations = [
        migrations.AlterField(
            model_name='phonenumberdb',
            name='number',
            field=models.CharField(max_length=10, db_index=True),
        ),
    ]
