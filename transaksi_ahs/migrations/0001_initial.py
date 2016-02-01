# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-01-30 10:16
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('setting_proyek', '0004_auto_20160123_0412'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('element', '0012_auto_20160130_0807'),
    ]

    operations = [
        migrations.CreateModel(
            name='AHS',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nomor_ahs', models.CharField(max_length=7, unique=True)),
                ('nama_ahs', models.CharField(max_length=120)),
                ('harga_satuan', models.FloatField()),
                ('koefisien', models.FloatField()),
                ('catatan', models.TextField(blank=True, max_length=200)),
                ('updated_date', models.DateTimeField(auto_now=True)),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='ahs_created_by', to=settings.AUTH_USER_MODEL)),
                ('kode_element', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='element.Element')),
                ('nomor_proyek', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='setting_proyek.Proyek')),
                ('updated_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='ahs_updated_by', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]