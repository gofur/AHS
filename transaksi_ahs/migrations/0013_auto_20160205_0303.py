# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-02-05 03:03
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('transaksi_ahs', '0012_auto_20160205_0302'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ahs',
            name='satuan_ahs',
            field=models.CharField(blank=True, max_length=10),
        ),
    ]