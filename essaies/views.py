from django.shortcuts import render

from django.shortcuts import render
from rest_framework.decorators import api_view
from users.serializers import PaiementSerializer, Utilisateur2Serializer,Type_AbonnementSerializer
from essaies.models import *
from rest_framework.response import Response
from rest_framework import status
import urllib.parse
import urllib.request
import ssl
from django.http import HttpResponse
from users.models import *






@api_view(['GET'])
def insertionEssaie(request):

    u = personne_essaie.objects.values('id', 'prenom', 'nom', 'date_created', 'telephone', 'civilte', 'email')
    print(u)
    for e1 in u:

        id = e1['id']
        prenom = e1['prenom']
        nom = e1['nom']
        date_created = e1['date_created']
        telephone = e1['telephone']
        civilite = e1['civilte']
        email = e1['email']

        data = {
            'id':id,
            'prenom':prenom,
            'nom':nom,
            'date_created': date_created,
            'telephone': telephone,
            'civilite': civilite,
            'email': email
        }


        url = 'http://5.196.224.234:8000/insertionEssaieDatabase/'

        datas = urllib.parse.urlencode(data)
        datas = datas.encode('utf-8')
        req = urllib.request.Request(url, datas)
        response = urllib.request.urlopen(req)
        the_page = response.read()



    return Response(data={
                    'status': 0,
                    'message': 'La synchronisation de la base de donnée locale sur la base distante est bien effectuée.'
                })




@api_view(['POST'])
def insertionEssaieDatabase(request):

    if request.method == "POST":


        ids = request.data['id']
        prenom = request.data['prenom']
        nom = request.data['nom']
        date_created = request.data['date_created']
        telephone = request.data['telephone']
        civilite = request.data['civilite']
        email = request.data['email']


        personne_essaiess = personne_essaie()
        personne_essaiess.id = ids
        personne_essaiess.nom = nom
        personne_essaiess.prenom = prenom
        personne_essaiess.date_created = date_created
        personne_essaiess.civilte = civilite
        personne_essaiess.telephone = telephone
        personne_essaiess.email = email
        personne_essaiess.save()


        return Response(data={
                        'status': 0,
                        'message': ' L\' enregistrement des Types d abonnements est bien effectuée.'
                    })




@api_view(['GET'])
def nombrePersonneEssai(request):



    personne = personne_essaie.objects.count()
    #personne = utilisateur2.objects.filter()
    #personne = Paiement.objects.filter(idUser=utilisateur2__id)


    return Response(data={
                    'status': 0,
                    'nbAbonnees':personne,
                    'message': ' L\' enregistrement des Types d abonnements est bien effectuée. '
                })