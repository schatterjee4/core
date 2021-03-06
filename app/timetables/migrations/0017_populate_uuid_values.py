# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-10-24 16:16
from __future__ import unicode_literals

from django.db import migrations
import uuid

def gen_uuid(apps, schema_editor):
    MenuItem = apps.get_model('timetables', 'MenuItem')
    for row in MenuItem.objects.all():
        row.public_id = uuid.uuid4()
        row.save()

def gen_num(apps, schema_editor):
    Course = apps.get_model('timetables', 'Course')
    for i, row in enumerate(Course.objects.all()):
        row.sequence_order = i + 1970
        row.save()


class Migration(migrations.Migration):

    dependencies = [
        ('timetables', '0016_auto_20161025_0948'),
    ]

    operations = [
        migrations.RunPython(gen_uuid, reverse_code=migrations.RunPython.noop),
        migrations.RunPython(gen_num, reverse_code=migrations.RunPython.noop),
    ]
