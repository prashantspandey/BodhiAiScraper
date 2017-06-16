# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-06-04 09:11
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_auto_20170530_1821'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='headslug',
        ),
        migrations.AddField(
            model_name='post',
            name='category',
            field=models.CharField(choices=[(0, 'Sports'), (1, 'World-News'), (2, 'IndiaNews'), (3, 'Entertainment and Movies'), (4, 'Uncategorized')], default=4, max_length=50),
            preserve_default=False,
        ),
    ]
