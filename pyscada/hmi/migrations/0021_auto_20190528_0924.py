# -*- coding: utf-8 -*-
# Generated by Django 1.11.18 on 2019-05-28 09:24
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pyscada', '0054_auto_20190411_0749'),
        ('hmi', '0020_pie'),
    ]

    operations = [
        migrations.AddField(
            model_name='customhtmlpanel',
            name='variable_properties',
            field=models.ManyToManyField(blank=True, to='pyscada.VariableProperty'),
        ),
        migrations.AlterField(
            model_name='customhtmlpanel',
            name='variables',
            field=models.ManyToManyField(blank=True, to='pyscada.Variable'),
        ),
    ]
