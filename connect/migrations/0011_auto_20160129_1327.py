# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('connect', '0010_auto_20160129_1248'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='ProblemVotes',
            new_name='ProblemVote',
        ),
    ]
