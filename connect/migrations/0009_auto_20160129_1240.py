# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('connect', '0008_problemsolved'),
    ]

    operations = [
        migrations.CreateModel(
            name='Problem',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=150)),
                ('content', models.CharField(max_length=500)),
                ('bhavan', models.ForeignKey(to='connect.Bhavan')),
                ('solved_by', models.ForeignKey(related_name='solved_by', blank=True, to=settings.AUTH_USER_MODEL, null=True)),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'permissions': (('problem_solve', 'Add events custom'),),
            },
        ),
        migrations.RemoveField(
            model_name='problemsolved',
            name='bhavan',
        ),
        migrations.RemoveField(
            model_name='problemsolved',
            name='solved_by',
        ),
        migrations.RemoveField(
            model_name='problemsolved',
            name='user',
        ),
        migrations.DeleteModel(
            name='ProblemSolved',
        ),
    ]
