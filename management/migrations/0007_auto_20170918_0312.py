# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-09-18 03:12
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0003_auto_20170918_0312'),
        ('management', '0006_auto_20170918_0253'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='feesdetail',
            name='fees_information',
        ),
        migrations.DeleteModel(
            name='FeesDetail',
        ),
        migrations.DeleteModel(
            name='FeesInformation',
        ),
    ]
