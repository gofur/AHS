# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-02-05 03:02
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('transaksi_ahs', '0011_auto_20160205_0223'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ahs',
            name='kode_element',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='element.Element'),
        ),
        migrations.AlterField(
            model_name='ahs',
            name='nomor_proyek',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='setting_proyek.Proyek'),
        ),
    ]
