# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('connect', '0016_travel'),
    ]

    operations = [
        migrations.AlterField(
            model_name='travel',
            name='from_place',
            field=models.ForeignKey(related_name='from_place', to='connect.Place'),
        ),
        migrations.AlterField(
            model_name='travel',
            name='to_place',
            field=models.ForeignKey(related_name='to_place', to='connect.Place'),
        ),
    ]
