# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-02-05 03:04
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('transaksi_ahs', '0013_auto_20160205_0303'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ahs',
            name='nomor_ahs',
            field=models.CharField(max_length=7),
        ),
    ]
