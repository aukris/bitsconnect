# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('connect', '0012_remove_problemsolved_reply'),
    ]

    operations = [
        migrations.RenameField(
            model_name='problemsolved',
            old_name='content',
            new_name='reply',
        ),
    ]
