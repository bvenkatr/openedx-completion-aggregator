# -*- coding: utf-8 -*-
# Generated by Django 1.10.8 on 2018-12-17 19:04
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('completion_aggregator', '0004_index_stalecompletion'),
    ]

    operations = [
        migrations.CreateModel(
            name='CacheGroupInvalidation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('group', models.CharField(max_length=150, unique=True)),
                ('invalidated_at', models.DateTimeField(db_index=True)),
            ],
        ),
    ]
