# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-01-31 03:42
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('transaksi_ahs', '0003_auto_20160131_0341'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ahs',
            name='nomor_proyek',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='setting_proyek.Proyek'),
        ),
    ]