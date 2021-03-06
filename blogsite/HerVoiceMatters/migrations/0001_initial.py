# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-05-13 12:35
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default=' ', max_length=200)),
                ('event_date', models.DateTimeField()),
                ('location', models.CharField(max_length=150)),
                ('description', models.TextField(max_length=800)),
                ('height_img', models.IntegerField(default=0)),
                ('width_img', models.IntegerField(default=0)),
                ('image_field', models.ImageField(blank=True, height_field='height_img', null=True, upload_to='events/', width_field='width_img')),
                ('Attending', models.IntegerField(default=0)),
                ('organizer', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Gallery',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('height_img', models.IntegerField(default=30)),
                ('width_img', models.IntegerField(default=30)),
                ('image_field', models.ImageField(blank=True, height_field='height_img', null=True, upload_to='gallery/', width_field='width_img')),
                ('description', models.CharField(max_length=300)),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('category', models.CharField(choices=[('fas', 'FASHION'), ('food', 'FOOD'), ('girl', 'GIRL TALK')], default='girl', max_length=5)),
                ('content', models.TextField()),
                ('height_img', models.IntegerField(default=0)),
                ('width_img', models.IntegerField(default=0)),
                ('image_field', models.ImageField(blank=True, height_field='height_img', null=True, upload_to='posts/', width_field='width_img')),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('author', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-created_date'],
            },
        ),
    ]
