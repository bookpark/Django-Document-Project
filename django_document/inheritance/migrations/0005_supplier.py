# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-11 08:08
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('inheritance', '0004_place_restaurant'),
    ]

    operations = [
        migrations.CreateModel(
            name='Supplier',
            fields=[
                ('place_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='inheritance.Place')),
                ('customers', models.ManyToManyField(related_name='customer_place_set', to='inheritance.Place')),
            ],
            bases=('inheritance.place',),
        ),
    ]
