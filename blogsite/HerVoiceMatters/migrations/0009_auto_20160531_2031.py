# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-05-31 17:31
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('HerVoiceMatters', '0008_auto_20160527_1440'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='category',
            field=models.CharField(choices=[('fashion', 'FASHION'), ('food', 'FOOD'), ('girl', 'GIRL TALK')], default='girl', max_length=7),
        ),
    ]
