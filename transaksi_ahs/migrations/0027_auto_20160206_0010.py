# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-02-06 00:10
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('transaksi_ahs', '0026_ahs_total_harga'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ahs',
            name='total_harga',
            field=models.FloatField(),
        ),
    ]
