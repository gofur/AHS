# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-01-30 08:05
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('element', '0009_auto_20160130_0803'),
    ]

    operations = [
        migrations.RenameField(
            model_name='jeniselement',
            old_name='jenis_element',
            new_name='nama_jenis_element',
        ),
    ]