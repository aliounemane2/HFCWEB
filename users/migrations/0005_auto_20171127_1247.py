# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-11-27 12:47
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_utilisateur2_status_email'),
    ]

    operations = [
        migrations.RenameField(
            model_name='utilisateur2',
            old_name='status_email',
            new_name='status_emails',
        ),
    ]
