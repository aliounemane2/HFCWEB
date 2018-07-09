from django.db import models
import base64
from django.core.files.base import ContentFile
from django.conf import settings


from employers.models import *


# Register your models here.


class employers(models.Model):

    civilte = models.CharField(max_length=150)
    prenom = models.CharField(max_length=150)
    nom = models.CharField(max_length=150)
    profession = models.CharField(max_length=150)
    dateNaiss = models.CharField(max_length=35)
    carte_didentite_nationale = models.CharField(max_length=25, null=True, blank=True)
    telephone = models.CharField(max_length=50, null=True, blank=True)
    email = models.CharField(max_length=125, null=True, blank=True)
    adresse = models.CharField(max_length=125, null=True, blank=True)
    idcarte = models.IntegerField(default=0)
    prenom1 = models.CharField(max_length=125, null=True, blank=True)
    nom1 = models.CharField(max_length=125, null=True, blank=True)
    telephone1 = models.CharField(max_length=125, null=True, blank=True)
    prenom2 = models.CharField(max_length=125, null=True, blank=True)
    nom2 = models.CharField(max_length=125, null=True, blank=True)
    telephone2 = models.CharField(max_length=125, null=True, blank=True)
    ### photo = models.TextField(null=True, blank=True)
    #photo = models.FileField(null=True, upload_to='employers/')
    photo2 = models.FileField(null=True, upload_to='employers/')
    photo = models.TextField(null=True, blank=True)
    #photo2 = models.FileField(null=True, upload_to='employers/')


    def __str__(self):
        return str(self.telephone)

    @property
    def get_absolute_image_url(self):
        return "{0}{1}".format(settings.MEDIA_URL, self.photo2.url)



    @property
    def image_url(self):
        try:
            img = open(self.photo2.path, "rb")
            data = img.read()
            return "data:image/jpg;base64,%s" % data.encode('base64')

        except IOError:
            return self.photo2.url


    #@property
    #def image_url(self):
    #    try:
    #        img = open(self.image.path, "rb")
    #        data = img.read()
    #        return "data:image/jpg;base64,%s" % img.encode('base64')
    #    except IOError:
    #        return self.image.url



class pointage(models.Model):
    idUser = models.IntegerField()
    #idUser = models.ForeignKey(employers, on_delete=models.CASCADE)
    date_et_heures = models.CharField(max_length=30,  null=True, blank=True)
    #date_et_heures = models.CharField(max_length=30,  null=True, blank=True)


    def __str__(self):
        return str(self.date_et_heures)
