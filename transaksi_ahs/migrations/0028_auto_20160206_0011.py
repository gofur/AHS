# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-02-06 00:11
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('transaksi_ahs', '0027_auto_20160206_0010'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ahs',
            name='total_harga',
            field=models.FloatField(blank=True),
        ),
    ]