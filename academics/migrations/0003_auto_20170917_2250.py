# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-09-17 22:50
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('academics', '0002_auto_20170917_2027'),
    ]

    operations = [
        migrations.RenameField(
            model_name='academic',
            old_name='sem_no',
            new_name='semester',
        ),
    ]
