# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-10-09 18:41
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('orm', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Kriteria',
            new_name='Alternatif',
        ),
        migrations.AlterModelTable(
            name='alternatif',
            table='alternatif',
        ),
    ]