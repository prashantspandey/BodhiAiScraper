# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-06-05 11:43
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0009_post_summary'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='summary',
            field=models.CharField(blank=True, max_length=1000, null=True),
        ),
    ]