# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-01-21 14:13
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('element', '0002_element_kode_element'),
    ]

    operations = [
        migrations.AddField(
            model_name='element',
            name='harga_satuan',
            field=models.DecimalField(decimal_places=2, default=1, max_digits=5),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='element',
            name='keterangan',
            field=models.TextField(blank=True, max_length=200),
        ),
    ]
