# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-05-24 11:17
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('HerVoiceMatters', '0005_auto_20160524_1336'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='category',
            field=models.CharField(choices=[('fashion', 'FASHION'), ('dish', 'FOOD'), ('girl', 'GIRL TALK')], default='girl', max_length=7),
        ),
    ]
