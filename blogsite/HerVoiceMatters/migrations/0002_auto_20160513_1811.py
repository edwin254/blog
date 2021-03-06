# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-05-13 15:11
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('HerVoiceMatters', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='event',
            options={'ordering': ['-event_date']},
        ),
        migrations.AlterModelOptions(
            name='gallery',
            options={'ordering': ['-created_date']},
        ),
        migrations.AlterField(
            model_name='event',
            name='height_img',
            field=models.IntegerField(default=250),
        ),
        migrations.AlterField(
            model_name='event',
            name='width_img',
            field=models.IntegerField(default=250),
        ),
        migrations.AlterField(
            model_name='gallery',
            name='height_img',
            field=models.IntegerField(default=300),
        ),
        migrations.AlterField(
            model_name='gallery',
            name='width_img',
            field=models.IntegerField(default=300),
        ),
        migrations.AlterField(
            model_name='post',
            name='height_img',
            field=models.IntegerField(default=300),
        ),
        migrations.AlterField(
            model_name='post',
            name='width_img',
            field=models.IntegerField(default=300),
        ),
    ]
