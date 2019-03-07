# -*- coding: utf-8 -*-
# Generated by Django 1.11.18 on 2019-02-06 15:07
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('modbus', '0007_extendedmodbusdevice_extendedmodbusvariable'),
    ]

    operations = [
        migrations.AddField(
            model_name='modbusdevice',
            name='framer',
            field=models.PositiveSmallIntegerField(blank=True, choices=[(0, 'Socket'), (1, 'RTU'), (2, 'ASCII'), (3, 'Binary')], null=True),
        ),
    ]