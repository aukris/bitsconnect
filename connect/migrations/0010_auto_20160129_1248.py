# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('connect', '0009_auto_20160129_1240'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProblemSolved',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=150)),
                ('content', models.CharField(max_length=500)),
                ('reply', models.CharField(max_length=500)),
                ('bhavan', models.ForeignKey(to='connect.Bhavan')),
                ('solved_by', models.ForeignKey(related_name='solved_by', blank=True, to=settings.AUTH_USER_MODEL, null=True)),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='ProblemVotes',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='problem',
            name='solved_by',
        ),
        migrations.AddField(
            model_name='problem',
            name='votes',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='problemvotes',
            name='problem',
            field=models.ForeignKey(to='connect.Problem'),
        ),
        migrations.AddField(
            model_name='problemvotes',
            name='user',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterUniqueTogether(
            name='problemvotes',
            unique_together=set([('problem', 'user')]),
        ),
    ]
