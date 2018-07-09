from django.db import models

class adminss(models.Model):

    prenom = models.CharField(max_length=150)
    nom = models.CharField(max_length=150)
    telephone = models.CharField(max_length=30, unique=True,null=True)
    activation_token = models.CharField(max_length=6, null=True)
    is_active = models.BooleanField(default=True)
    email = models.CharField(max_length=255, null=True, unique=True)
    password = models.CharField(max_length=255, null=True, blank=True)


    def __str__(self):
        return str(self.email)