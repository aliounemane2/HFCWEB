from django.db import models


class utilisateur2(models.Model):

    civilite = models.CharField(max_length=100, null=True, blank=True)
    prenom = models.CharField(max_length=150)
    nom = models.CharField(max_length=150)
    dateNaiss = models.CharField(max_length=22, null=True, blank=True)
    lieuNaiss = models.CharField(max_length=130, null=True, blank=True)
    adresse = models.CharField(max_length=175, null=True, blank=True)
    ville = models.CharField(max_length=150, null=True, blank=True)
    email = models.CharField(max_length=150, null=True, blank=True)
    profession = models.CharField(max_length=125, null=True, blank=True)
    prenom1 = models.CharField(max_length=125, null=True, blank=True)
    nom1 = models.CharField(max_length=125, null=True, blank=True)
    telephone1 = models.CharField(max_length=40, null=True , blank=True)
    prenom2 = models.CharField(max_length=125, null=True, blank=True)
    nom2 = models.CharField(max_length=125, null=True, blank=True)
    telephone2 = models.CharField(max_length=125, null=True, blank=True)
    idcarte = models.IntegerField()
    telephone = models.CharField(max_length=50, blank=True, null=True)
    id_typeabonnement = models.IntegerField()
    photo = models.TextField(null=True, blank=True)
    # status_email = models.CharField(max_length=1, blank=True, null=True)
    status_email = models.CharField(max_length=1, default='1')


    def __str__(self):
        return str(self.telephone)



class Type_Abonnement(models.Model):

    nom = models.CharField(max_length=175, null=True, blank=True)
    montant = models.IntegerField()

    def __str__(self):
        return str(self.nom)




class Paiement(models.Model):
    idPaiement = models.AutoField(primary_key=True)
    date_debut = models.CharField(max_length=22, null=True, blank=True)
    date_fin = models.CharField(max_length=22, null=True, blank=True)
    #idUser = models.IntegerField()
    idUser = models.ForeignKey(utilisateur2, on_delete=models.CASCADE)
    nbseances_en_cours = models.IntegerField(default=0)
    nbseances_total = models.IntegerField(default=0)
    dateencours = models.CharField(max_length=22,  null=True, blank=True)
    date_autorisation = models.CharField(max_length=22, null=True, blank=True)
    datebadge = models.CharField(max_length=32, null=True, blank=True)


    def __str__(self):
        return str(self.idPaiement)



class Statisque(models.Model):
    idUser = models.ForeignKey(utilisateur2, on_delete=models.CASCADE)
    date_heure = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return str(self.date_heure)



class Parrainage(models.Model):
    parrain = models.ForeignKey(utilisateur2, on_delete=models.CASCADE, related_name='parrain')
    filleul = models.ForeignKey(utilisateur2, on_delete=models.CASCADE, related_name='filleul')
    date_heure_parrainage = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return str(self.date_heure_parrainage)

