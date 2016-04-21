# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('connect', '0017_auto_20160130_1924'),
    ]

    operations = [
        migrations.AddField(
            model_name='travel',
            name='content',
            field=models.CharField(max_length=150, null=True),
        ),
        migrations.AddField(
            model_name='travel',
            name='user',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL, null=True),
        ),
    ]
