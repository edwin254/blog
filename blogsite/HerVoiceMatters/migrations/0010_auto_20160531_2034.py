# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-05-31 17:34
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('HerVoiceMatters', '0009_auto_20160531_2031'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='category',
            field=models.CharField(choices=[('fashion', 'FASHION'), ('delicacies', 'FOOD'), ('women', 'GIRL TALK')], default='girl', max_length=7),
        ),
    ]
