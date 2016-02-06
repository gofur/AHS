# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-02-05 22:50
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('transaksi_ahs', '0020_auto_20160205_0718'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ahs_detail',
            name='kode_element',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Kode_Element', to='element.Element'),
        ),
        migrations.AlterField(
            model_name='ahs_detail',
            name='nomor_ahs',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Nomor_AHS', to='transaksi_ahs.AHS'),
        ),
    ]