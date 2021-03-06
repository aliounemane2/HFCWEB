# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-10-17 14:00
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Paiement',
            fields=[
                ('idPaiement', models.AutoField(primary_key=True, serialize=False)),
                ('date_debut', models.CharField(blank=True, max_length=22, null=True)),
                ('date_fin', models.CharField(blank=True, max_length=22, null=True)),
                ('idUser', models.IntegerField()),
                ('nbseances_en_cours', models.IntegerField(default=0)),
                ('nbseances_total', models.IntegerField(default=0)),
                ('dateencours', models.CharField(blank=True, max_length=22, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Type_Abonnement',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(blank=True, max_length=175, null=True)),
                ('montant', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='utilisateur2',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('civilite', models.CharField(blank=True, max_length=100, null=True)),
                ('prenom', models.CharField(max_length=150)),
                ('nom', models.CharField(max_length=150)),
                ('dateNaiss', models.CharField(blank=True, max_length=22, null=True)),
                ('lieuNaiss', models.CharField(blank=True, max_length=130, null=True)),
                ('adresse', models.CharField(blank=True, max_length=175, null=True)),
                ('ville', models.CharField(blank=True, max_length=150, null=True)),
                ('email', models.CharField(blank=True, max_length=150, null=True)),
                ('profession', models.CharField(blank=True, max_length=125, null=True)),
                ('prenom1', models.CharField(blank=True, max_length=125, null=True)),
                ('nom1', models.CharField(blank=True, max_length=125, null=True)),
                ('telephone1', models.CharField(blank=True, max_length=40, null=True)),
                ('prenom2', models.CharField(blank=True, max_length=125, null=True)),
                ('nom2', models.CharField(blank=True, max_length=125, null=True)),
                ('telephone2', models.CharField(blank=True, max_length=125, null=True)),
                ('idcarte', models.IntegerField()),
                ('telephone', models.CharField(blank=True, max_length=50, null=True)),
                ('id_typeabonnement', models.IntegerField()),
                ('photo', models.TextField(blank=True, null=True)),
            ],
        ),
    ]
