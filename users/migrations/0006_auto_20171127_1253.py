# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-11-27 12:53
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_auto_20171127_1247'),
    ]

    operations = [
        migrations.RenameField(
            model_name='utilisateur2',
            old_name='status_emails',
            new_name='status_email',
        ),
    ]