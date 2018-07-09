from django.db import models

# Create your models here.

from essaies.models import *


class personne_essaie(models.Model):

    civilte = models.CharField(max_length=150, null=True, blank=True)
    prenom = models.CharField(max_length=150)
    nom = models.CharField(max_length=150)
    date_created = models.DateTimeField(null=True, blank=True)
    telephone = models.CharField(max_length=50, unique=True, null=True)
    email = models.CharField(max_length=255, null=True, blank=True)


    def __str__(self):
        return str(self.telephone)