# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-02-04 20:58
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('transaksi_ahs', '0005_auto_20160204_2046'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ahs',
            name='nomor_ahs',
            field=models.CharField(max_length=7, unique=True),
        ),
        migrations.AlterField(
            model_name='ahs',
            name='nomor_proyek',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='setting_proyek.Proyek', unique=True),
        ),
    ]
