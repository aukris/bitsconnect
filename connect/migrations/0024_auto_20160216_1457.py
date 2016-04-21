# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('connect', '0023_missedcall_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bhavan',
            name='name',
            field=models.CharField(max_length=10, db_index=True),
        ),
        migrations.AlterField(
            model_name='classified',
            name='created',
            field=models.DateTimeField(auto_now_add=True, db_index=True),
        ),
        migrations.AlterField(
            model_name='event',
            name='time',
            field=models.DateTimeField(db_index=True),
        ),
        migrations.AlterField(
            model_name='problem',
            name='votes',
            field=models.IntegerField(default=0, db_index=True),
        ),
        migrations.AlterField(
            model_name='problemsolved',
            name='solved_on',
            field=models.DateTimeField(auto_now_add=True, db_index=True),
        ),
        migrations.AlterField(
            model_name='service',
            name='created',
            field=models.DateTimeField(auto_now_add=True, db_index=True),
        ),
        migrations.AlterField(
            model_name='travel',
            name='date',
            field=models.DateTimeField(db_index=True),
        ),
    ]
