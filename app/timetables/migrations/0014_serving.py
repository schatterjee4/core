# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-10-13 12:32
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('timetables', '0013_timetable_inactive_weekdays'),
    ]

    operations = [
        migrations.CreateModel(
            name='Serving',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('date_modified', models.DateTimeField(auto_now=True)),
                ('date_served', models.DateTimeField()),
                ('menu_item', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='timetables.MenuItem')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
