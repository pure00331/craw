# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-10-23 14:30
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('a01', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='perform',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.CharField(max_length=30)),
                ('title', models.CharField(max_length=30)),
                ('summary', models.TextField()),
            ],
        ),
        migrations.DeleteModel(
            name='Person',
        ),
    ]
