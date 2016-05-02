# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('connect', '0028_auto_20160503_0146'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='bookorder',
            options={'ordering': ('-id',)},
        ),
        migrations.AddField(
            model_name='bookorder',
            name='approved_by',
            field=models.ForeignKey(related_name='approved_by', blank=True, to=settings.AUTH_USER_MODEL, null=True),
        ),
        migrations.AlterField(
            model_name='book',
            name='title',
            field=models.CharField(max_length=200),
        ),
    ]
