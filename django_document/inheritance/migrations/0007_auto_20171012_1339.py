# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-12 04:39
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inheritance', '0006_auto_20171011_1739'),
    ]

    operations = [
        migrations.CreateModel(
            name='Midliner',
            fields=[
            ],
            options={
                'proxy': True,
                'indexes': [],
            },
            bases=('inheritance.champion',),
        ),
        migrations.CreateModel(
            name='Supporter',
            fields=[
            ],
            options={
                'ordering': ['name'],
                'proxy': True,
                'indexes': [],
            },
            bases=('inheritance.champion',),
        ),
        migrations.AlterModelOptions(
            name='champion',
            options={'ordering': ['rank']},
        ),
        migrations.RemoveField(
            model_name='supplier',
            name='customers',
        ),
        migrations.AddField(
            model_name='supplier',
            name='supply_places',
            field=models.ManyToManyField(related_name='supply_place_set', related_query_name='supply_place', to='inheritance.Place'),
        ),
    ]
