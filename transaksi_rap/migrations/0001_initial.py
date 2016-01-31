# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-01-30 15:44
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('transaksi_ahs', '0002_auto_20160130_1022'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='RAP',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('volume_rab', models.IntegerField()),
                ('harga_satuan_rab', models.FloatField()),
                ('volume_rap', models.IntegerField()),
                ('catatan', models.TextField(blank=True, max_length=200)),
                ('updated_date', models.DateTimeField(auto_now=True)),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='rap_created_by', to=settings.AUTH_USER_MODEL)),
                ('nomor_ahs', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='transaksi_ahs.AHS')),
                ('updated_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='rap_updated_by', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
