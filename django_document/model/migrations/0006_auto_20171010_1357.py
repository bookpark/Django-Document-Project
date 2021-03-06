# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-10 04:57
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('model', '0005_auto_20171010_0321'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('spouse', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='model.User')),
            ],
        ),
        migrations.AlterField(
            model_name='car',
            name='name',
            field=models.CharField(blank=True, max_length=50),
        ),
    ]
