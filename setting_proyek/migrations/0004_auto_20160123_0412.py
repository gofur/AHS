# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-01-23 04:12
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('setting_proyek', '0003_auto_20160122_0019'),
    ]

    operations = [
        migrations.AlterField(
            model_name='proyek',
            name='pengguna',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
