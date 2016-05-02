# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('connect', '0025_auto_20160502_2317'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='PhoneNumber',
            new_name='PhoneNumberDB',
        ),
        migrations.AddField(
            model_name='bookorder',
            name='user',
            field=models.ForeignKey(default=1, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]
