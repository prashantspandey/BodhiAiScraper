# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-05-30 10:20
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tags',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tag', models.CharField(max_length=10)),
                ('posttag', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.Post')),
            ],
        ),
    ]
