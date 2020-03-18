# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2020-03-18 06:31
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('s_name', models.CharField(max_length=16)),
                ('s_pic', models.ImageField(upload_to='s_icons')),
            ],
        ),
    ]
