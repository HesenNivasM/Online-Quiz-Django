# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2018-09-17 18:35
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='multiplechoicequestions',
            name='username',
        ),
        migrations.RemoveField(
            model_name='textquestions',
            name='username',
        ),
    ]
