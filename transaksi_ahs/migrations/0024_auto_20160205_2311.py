# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-02-05 23:11
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('transaksi_ahs', '0023_auto_20160205_2304'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ahs_detail',
            name='kode_element',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='element.Element'),
        ),
    ]