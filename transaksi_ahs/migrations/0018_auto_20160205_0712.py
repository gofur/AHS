# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-02-05 07:12
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('transaksi_ahs', '0017_auto_20160205_0707'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ahs_detail',
            name='kode_element',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='element.Element', unique=True),
        ),
        migrations.AlterField(
            model_name='ahs_detail',
            name='nomor_ahs',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='transaksi_ahs.AHS', unique=True),
        ),
    ]
