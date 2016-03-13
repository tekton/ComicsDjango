# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-03-13 07:01
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('issues', '0002_series_series_max_date'),
        ('comicFiles', '0002_comicfile_primary'),
    ]

    operations = [
        migrations.AddField(
            model_name='comicfile',
            name='series',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='issues.Series'),
        ),
    ]
