# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('connect', '0019_auto_20160130_2108'),
    ]

    operations = [
        migrations.AlterField(
            model_name='classified',
            name='title',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='event',
            name='title',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='problem',
            name='title',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='problemsolved',
            name='title',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='service',
            name='title',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='travel',
            name='content',
            field=models.CharField(max_length=200),
        ),
    ]
