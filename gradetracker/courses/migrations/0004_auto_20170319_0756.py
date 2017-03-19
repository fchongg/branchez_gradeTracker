# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-19 14:56
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0003_auto_20170319_0044'),
    ]

    operations = [
        migrations.AlterField(
            model_name='assessment',
            name='agid',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='courses.AssessmentGroup', verbose_name='Type of Assessment'),
        ),
        migrations.AlterField(
            model_name='assessment',
            name='aname',
            field=models.CharField(max_length=200, verbose_name='Name'),
        ),
        migrations.AlterField(
            model_name='assessment',
            name='apercentage',
            field=models.PositiveSmallIntegerField(verbose_name='Percentage of Assessment Group'),
        ),
    ]
