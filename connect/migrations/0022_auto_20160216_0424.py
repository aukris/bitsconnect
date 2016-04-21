# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('connect', '0021_globalevent'),
    ]

    operations = [
        migrations.CreateModel(
            name='MissedCall',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('actor', models.ForeignKey(related_name='caller', to=settings.AUTH_USER_MODEL)),
                ('user', models.ForeignKey(related_name='callee', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AlterField(
            model_name='problemvote',
            name='problem',
            field=models.ForeignKey(related_name='voters', to='connect.Problem'),
        ),
    ]
