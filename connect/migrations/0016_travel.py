# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('connect', '0015_auto_20160130_1910'),
    ]

    operations = [
        migrations.CreateModel(
            name='Travel',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('from_place', models.IntegerField(choices=[(1, b'pilani'), (2, b'delhi'), (3, b'jaipur'), (4, b'chandigarh')])),
                ('to_place', models.IntegerField(choices=[(1, b'pilani'), (2, b'delhi'), (3, b'jaipur'), (4, b'chandigarh')])),
                ('date', models.DateTimeField()),
            ],
        ),
    ]
