# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-02-05 02:17
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('transaksi_ahs', '0008_auto_20160204_2058'),
    ]

    operations = [
        migrations.AddField(
            model_name='ahs',
            name='satuan_ahs',
            field=models.CharField(default=1, max_length=10),
            preserve_default=False,
        ),
    ]
