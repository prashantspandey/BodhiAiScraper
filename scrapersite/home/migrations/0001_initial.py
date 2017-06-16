# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-05-30 08:12
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('headline', models.CharField(max_length=500)),
                ('body', models.TextField()),
                ('pub_date', models.DateTimeField()),
            ],
        ),
    ]
