# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-09-20 15:47
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('timetables', '0009_auto_20160919_1218'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='dish',
            options={'verbose_name_plural': 'Dishes'},
        ),
        migrations.AddField(
            model_name='course',
            name='slug',
            field=models.SlugField(editable=False, max_length=150, null=True, unique=True),
        ),
        migrations.AddField(
            model_name='dish',
            name='slug',
            field=models.SlugField(editable=False, max_length=255, null=True, unique=True),
        ),
        migrations.AddField(
            model_name='meal',
            name='slug',
            field=models.SlugField(editable=False, max_length=60, null=True, unique=True),
        ),
        migrations.AddField(
            model_name='mealoption',
            name='slug',
            field=models.SlugField(editable=False, max_length=120, null=True, unique=True),
        ),
        migrations.AddField(
            model_name='timetable',
            name='slug',
            field=models.SlugField(editable=False, max_length=255, null=True, unique=True),
        ),
        migrations.AddField(
            model_name='weekday',
            name='slug',
            field=models.SlugField(editable=False, max_length=60, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='course',
            name='name',
            field=models.CharField(max_length=150),
        ),
        migrations.AlterField(
            model_name='dish',
            name='name',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='meal',
            name='name',
            field=models.CharField(max_length=60),
        ),
        migrations.AlterField(
            model_name='mealoption',
            name='name',
            field=models.CharField(max_length=120),
        ),
        migrations.AlterField(
            model_name='timetable',
            name='name',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='weekday',
            name='name',
            field=models.CharField(max_length=60),
        ),
    ]
