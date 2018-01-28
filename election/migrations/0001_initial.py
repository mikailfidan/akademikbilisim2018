# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-01-28 12:14
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='Kategori Adı')),
                ('desc', models.CharField(max_length=250, verbose_name='Kategori Açıklaması')),
                ('created_at', models.DateTimeField(auto_now=True, verbose_name='Oluşturma Tarihi')),
            ],
            options={
                'verbose_name': 'Kategori',
                'verbose_name_plural': 'Kategoriler',
            },
        ),
        migrations.CreateModel(
            name='Survey',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Araştırma Adı')),
                ('active', models.BooleanField(default=False, verbose_name='Aktif mi?')),
                ('created_at', models.DateTimeField(auto_now=True, null=True, verbose_name='Oluşturulma Tarihi')),
                ('updated_at', models.DateTimeField(auto_now_add=True, null=True, verbose_name='Güncellenme Tarihi')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='election.Category', verbose_name='Kategori')),
            ],
            options={
                'verbose_name': 'Araştırma',
                'verbose_name_plural': 'Araştırmalar',
            },
        ),
    ]
