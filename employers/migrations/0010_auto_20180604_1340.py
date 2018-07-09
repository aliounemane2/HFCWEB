# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2018-06-04 13:40
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employers', '0009_remove_employers_photo2'),
    ]

    operations = [
        migrations.AddField(
            model_name='employers',
            name='photo2',
            field=models.FileField(null=True, upload_to='employers/'),
        ),
        migrations.AlterField(
            model_name='employers',
            name='photo',
            field=models.TextField(blank=True, null=True),
        ),
    ]
