# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('connect', '0024_auto_20160216_1457'),
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='BookOrder',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('is_delivered', models.BooleanField(default=False, help_text=b'Tick this if the book got delivered')),
                ('is_approved', models.BooleanField(default=False, help_text=b'Tick this to approve delivery')),
                ('room_no', models.IntegerField(default=0)),
                ('num_books', models.IntegerField()),
                ('comments', models.CharField(help_text=b'Guide the delivery boy', max_length=200)),
                ('bhavan', models.ForeignKey(to='connect.Bhavan')),
                ('book', models.ForeignKey(to='connect.Book')),
            ],
        ),
        migrations.CreateModel(
            name='PhoneNumber',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100, db_index=True)),
                ('designation', models.CharField(max_length=100)),
                ('number', models.IntegerField(db_index=True)),
            ],
        ),
        migrations.AlterModelOptions(
            name='problem',
            options={'permissions': (('problem_solve', 'Solve problems SU'),)},
        ),
    ]
