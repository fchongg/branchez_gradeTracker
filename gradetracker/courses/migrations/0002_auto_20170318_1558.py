# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-18 22:58
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='agtype',
            name='agtid',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='assessment',
            name='apercentage',
            field=models.PositiveSmallIntegerField(),
        ),
        migrations.AlterField(
            model_name='assessmentgroup',
            name='agid',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='assessmentgroup',
            name='agpercentage',
            field=models.PositiveSmallIntegerField(),
        ),
        migrations.AlterField(
            model_name='course',
            name='cid',
            field=models.IntegerField(),
        ),
    ]
