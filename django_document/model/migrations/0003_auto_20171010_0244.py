# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-10 02:44
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('model', '0002_fruits'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Fruits',
            new_name='Fruit',
        ),
    ]
