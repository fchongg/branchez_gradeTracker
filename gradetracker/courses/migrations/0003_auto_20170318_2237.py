# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-19 05:37
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('courses', '0002_auto_20170318_1558'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='agtype',
            name='agtid',
        ),
        migrations.RemoveField(
            model_name='assessment',
            name='agtid',
        ),
        migrations.RemoveField(
            model_name='assessmentgroup',
            name='agid',
        ),
        migrations.RemoveField(
            model_name='course',
            name='cid',
        ),
        migrations.AddField(
            model_name='assessment',
            name='duedate',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='Due Date'),
        ),
        migrations.AddField(
            model_name='course',
            name='uid',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='course',
            name='cname',
            field=models.CharField(max_length=200),
        ),
    ]
