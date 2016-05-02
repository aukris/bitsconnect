# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('connect', '0027_auto_20160502_2346'),
    ]

    operations = [
        migrations.RenameField(
            model_name='bookorder',
            old_name='num_books',
            new_name='nos',
        ),
        migrations.RemoveField(
            model_name='bookorder',
            name='bhavan',
        ),
        migrations.RemoveField(
            model_name='bookorder',
            name='comments',
        ),
        migrations.RemoveField(
            model_name='bookorder',
            name='room_no',
        ),
        migrations.AddField(
            model_name='bookorder',
            name='address',
            field=models.CharField(default='', help_text=b'Guide the delivery boy', max_length=250),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='bookorder',
            name='phone',
            field=models.CharField(default=0, help_text=b'Phone Number', max_length=10),
            preserve_default=False,
        ),
    ]
