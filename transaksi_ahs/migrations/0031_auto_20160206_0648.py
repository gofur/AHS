# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-02-06 06:48
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('transaksi_ahs', '0030_auto_20160206_0547'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ahs_detail',
            name='element',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='element_details', to='element.Element'),
        ),
    ]
