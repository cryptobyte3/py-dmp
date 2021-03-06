# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-06-13 15:28
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('data_loader', '0016_analyticsdatasource'),
    ]

    operations = [
        migrations.CreateModel(
            name='SpreadsheetsDataSource',
            fields=[
                ('data_source', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='data_loader.DataSource')),
                ('worksheet_id', models.CharField(default=None, max_length=255, verbose_name='Account ID')),
                ('upload_file', models.FileField(default=None, upload_to='file_uploads', verbose_name='Upload file')),
                ('document_url', models.CharField(default=None, max_length=355, verbose_name='Document URL')),
            ],
            options={
                'verbose_name_plural': 'Google Analytics Data source',
                'verbose_name': 'Google Analytics Data source',
            },
            bases=('data_loader.datasource',),
        ),
    ]
