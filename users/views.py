from django.shortcuts import render
from rest_framework.decorators import api_view
from users.serializers import PaiementSerializer, Utilisateur2Serializer,Type_AbonnementSerializer
from users.models import *
from rest_framework.response import Response
from rest_framework import status
import urllib.parse
import urllib.request
import ssl
from django.http import HttpResponse
from adminsss.serializers import *
from django.db import connection
from datetime import datetime, timedelta
from django.db.models import Count
from datetime import datetime
from employers.models import *





@api_view(['GET'])
def idcarte(request):

    #### Cette fonction permet d'insérer des utilisateurs de la base de donnée locale sur la base de donnée distante

    u = utilisateur2.objects.values('id','idcarte')
    print(u)

    return Response(data={
                    'status': 0,
                    'data':u,
                    'message': 'La synchronisation de la base de donnée locale sur la base distante est bien effectuée.'
                })





@api_view(['GET'])
def insertionIdCarte(request):

    if request.method == "GET":

        url = 'http://127.0.0.1:8000/idcarte/'

        print(' url ')
        print(' url ')
        print(url)
        print(url)
        #datas = urllib.parse.urlencode(data)
        #datas = datas.encode('utf-8')
        req = urllib.request.Request(url)
        print(req)
        response = urllib.request.urlopen(req)

        for inds in urllib.request.urlopen(req):
            print(' inds ')
            print(' inds ')
            print(inds)

        the_page = response.read()


        #users = utilisateur2.objects.get(id=)

        #users.idcarte = idcarte
        #users.save()

        return Response(data={
                        'status': 0,
                        'message': ' L\' enregistrement est bien effectuée. '
                    })






@api_view(['GET'])
def insertionUser2(request):

    #### Cette fonction permet d'insérer des utilisateurs de la base de donnée locale sur la base de donnée distante

    u = utilisateur2.objects.values('id', 'civilite', 'prenom', 'nom', 'dateNaiss', 'lieuNaiss', 'adresse', 'ville', 'email',
                                    'profession', 'prenom1', 'nom1', 'telephone1', 'prenom2', 'nom2', 'telephone2', 'idcarte',
                                    'telephone', 'id_typeabonnement', 'photo', 'status_email')
    print(u)
    for e1 in u:

        id = e1['id']
        civilite = e1['civilite']
        prenom = e1['prenom']
        nom = e1['nom']
        dateNaiss = e1['dateNaiss']
        lieuNaiss = e1['lieuNaiss']
        adresse = e1['adresse']
        ville = e1['ville']
        email = e1['email']
        profession = e1['profession']
        prenom1 = e1['prenom1']
        nom1 = e1['nom1']
        telephone1 = e1['telephone1']
        prenom2 = e1['prenom2']
        nom2 = e1['nom2']
        telephone2 = e1['telephone2']
        idcarte = e1['idcarte']
        telephone = e1['telephone']
        id_typeabonnement = e1['id_typeabonnement']
        photo = e1['photo']
        status_email = e1['status_email']


        data = {
            'id':id,
            'civilite':civilite,
            'prenom':prenom,
            'nom':nom,
            'dateNaiss':dateNaiss,
            'lieuNaiss':lieuNaiss,
            'adresse':adresse,
            'ville': ville,
            'email': email,
            'profession':profession,
            'prenom1': prenom1,
            'nom1': nom1,
            'telephone1': telephone1,
            'prenom2':prenom2,
            'nom2': nom2,
            'telephone2': telephone2,
            'idcarte': idcarte,
            'telephone': telephone,
            'id_typeabonnement': id_typeabonnement,
            'photo': photo,
            'status_email': status_email
        }


        url = 'http://5.196.224.234:8000/insertionDatabase/'
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
def insertionDatabase(request):

    if request.method == "POST":


        ids = request.data['id']
        civilite = request.data['civilite']
        prenom = request.data['prenom']
        nom = request.data['nom']
        dateNaiss = request.data['dateNaiss']
        lieuNaiss = request.data['lieuNaiss']
        adresse = request.data['adresse']
        ville = request.data['ville']
        email = request.data['email']
        profession = request.data['profession']
        prenom1 = request.data['prenom1']
        nom1 = request.data['nom1']
        telephone1 = request.data['telephone1']
        prenom2 = request.data['prenom2']
        nom2 = request.data['nom2']
        telephone2 = request.data['telephone2']
        idcarte = request.data['idcarte']
        telephone = request.data['telephone']
        id_typeabonnement = request.data['id_typeabonnement']
        photo = request.data['photo']
        status_email = request.data['status_email']

        users = utilisateur2()
        users.id = ids
        users.civilite = civilite
        users.prenom = prenom
        users.nom = nom
        users.dateNaiss = dateNaiss
        users.lieuNaiss = lieuNaiss
        users.adresse = adresse
        users.ville = ville
        users.email = email
        users.profession = profession
        users.prenom1 = prenom1
        users.nom1 = nom1
        users.telephone1 = telephone1
        users.prenom2 = prenom2
        users.nom2 = nom2
        users.telephone2 = telephone2
        users.idcarte = idcarte
        users.telephone = telephone
        users.id_typeabonnement = id_typeabonnement
        users.photo = photo
        users.status_email = status_email
        users.save()

        return Response(data={
                        'status': 0,
                        'message': ' L\' enregistrement est bien effectuée. '
                    })






@api_view(['GET'])
def insertionType_Abonnement(request):

    u = Type_Abonnement.objects.values('id', 'nom', 'montant')
    print(u)
    for e1 in u:

        id = e1['id']
        nom = e1['nom']
        montant = e1['montant']



        data = {
            'id':id,
            'nom':nom,
            'montant':montant
        }


        url = 'http://5.196.224.234:8000/insertionDatabaseTypeAbonnement/'
        #url = 'http://127.0.0.1:8000/insertionDatabaseTypeAbonnement/'

        datas = urllib.parse.urlencode(data)
        datas = datas.encode('utf-8')
        req = urllib.request.Request(url, datas)
        response = urllib.request.urlopen(req)
        the_page = response.read()

    return Response(data={
                    'status': 0,
                    'message': 'La synchronisation des types d abonnements de la base de donnée locale sur la base de donnée distante est bien effective.'
                })





@api_view(['POST'])
def insertionDatabaseTypeAbonnement(request):

    if request.method == "POST":



        ids = request.data['id']
        nom = request.data['nom']
        montant = request.data['montant']


        typeAbonnement = Type_Abonnement()
        typeAbonnement.id = ids
        typeAbonnement.nom = nom
        typeAbonnement.montant = montant

        typeAbonnement.save()

        return Response(data={
                        'status': 0,
                        'message': ' L\' enregistrement des Types d abonnements est bien effectuée. '
                    })




@api_view(['GET'])
def insertionPaiement(request):


    u = Paiement.objects.values('idPaiement', 'date_debut', 'date_fin', 'idUser', 'nbseances_en_cours', 'nbseances_total',
                                'dateencours', 'date_autorisation', 'datebadge')

    print(u)
    for e1 in u:
        idPaiement = e1['idPaiement']
        date_debut = e1['date_debut']
        date_fin = e1['date_fin']
        idUser = e1['idUser']
        nbseances_en_cours = e1['nbseances_en_cours']
        nbseances_total = e1['nbseances_total']
        dateencours = e1['dateencours']
        date_autorisation = e1['date_autorisation']
        datebadge = e1['datebadge']



        data = {
            'idPaiement':idPaiement,
            'date_debut':date_debut,
            'date_fin':date_fin,
            'idUser': idUser,
            'nbseances_en_cours': nbseances_en_cours,
            'nbseances_total': nbseances_total,
            'dateencours': dateencours,
            'date_autorisation': date_autorisation,
            'datebadge': datebadge
        }

        url = 'http://5.196.224.234:8000/insertionDatabasePaiement/'
        #url = 'http://127.0.0.1:8000/insertionDatabasePaiement/'

        datas = urllib.parse.urlencode(data)
        datas = datas.encode('utf-8')
        req = urllib.request.Request(url, datas)
        response = urllib.request.urlopen(req)
        the_page = response.read()

    return Response(data={
        'status': 0,
        'message': 'La synchronisation des types d abonnements de la base de donnée locale sur la base de donnée distante est bien effective.'
    })




@api_view(['POST'])
def insertionDatabasePaiement(request):

    if request.method == "POST":

        idPaiement = request.data['idPaiement']
        date_debut = request.data['date_debut']
        date_fin = request.data['date_fin']
        idUser = request.data['idUser']
        nbseances_en_cours = request.data['nbseances_en_cours']
        nbseances_total = request.data['nbseances_total']
        dateencours = request.data['dateencours']
        date_autorisation = request.data['date_autorisation']
        datebadge = request.data['datebadge']



        print('pas bon pas bon pas bon')
        print('pas bon pas bon pas bon')
        print('pas bon pas bon pas bon')
        if utilisateur2.objects.filter(id=idUser).count()==1:
            print('CEST BON CEST BON CEST BON ')
            print('CEST BON CEST BON CEST BON ')
            print('CEST BON CEST BON CEST BON ')
            paiement = Paiement()

            userrrr = utilisateur2.objects.get(id=idUser)

            paiement.idPaiement = idPaiement
            paiement.date_debut = date_debut
            paiement.date_fin = date_fin
            paiement.idUser = userrrr
            paiement.nbseances_en_cours = nbseances_en_cours
            paiement.nbseances_total = nbseances_total
            paiement.dateencours = dateencours
            paiement.date_autorisation = date_autorisation
            paiement.datebadge = datebadge
            paiement.save()


            return Response(data={
                            'status': 0,
                            'message': ' L\' enregistrement des Types d abonnements est bien effectuée.'
                        })
        else:
            return Response(data={
                'status': 0,
                'message': ' L\' enregistrement effectuée.'
            })





@api_view(['GET'])
def insertionStatistique(request):


    u = Statisque.objects.values('id', 'date_heure', 'idUser')

    print(u)
    for e1 in u:
        id = e1['id']
        date_heure = e1['date_heure']
        idUser = e1['idUser']


        data = {
            'id':id,
            'date_heure':date_heure,
            'idUser':idUser
        }
        print(' data ')
        print(' data ')
        print(' data ')
        print(data)
        #url = 'http://127.0.0.1:8000/insertionDatabaseStatistique/'
        url = 'http://5.196.224.234:8000/insertionDatabaseStatistique/'

        datas = urllib.parse.urlencode(data)
        datas = datas.encode('utf-8')
        req = urllib.request.Request(url, datas)
        response = urllib.request.urlopen(req)
        the_page = response.read()

    return Response(data={
        'status': 0,
        'message': 'La synchronisation des types d abonnements de la base de donnée locale sur la base de donnée distante est bien effective.'
    })



@api_view(['POST'])
def insertionDatabaseStatistique(request):

    if request.method == "POST":
        print(' POST POST POST ')
        date_heure = request.data['date_heure']
        id = request.data['id']
        idUser = request.data['idUser']

        print(date_heure)
        print(id)
        print(idUser)

        print('VALEUR DE LA TAILLE ')
        print('VALEUR DE LA TAILLE ')
        print('VALEUR DE LA TAILLE ')

        utilisateur2.objects.filter(id=idUser)




        if utilisateur2.objects.filter(id=idUser).count()==1:

            print('C BON C BON CB ON ')

            userrrr = utilisateur2.objects.get(id=idUser)
            statistique = Statisque()
            statistique.idUser = userrrr
            statistique.date_heure = date_heure
            statistique.id = id

            statistique.save()


            return Response(data={
                            'status': 0,
                            'message': ' L\' enregistrement des Entres et sorties est bien effectuée.'
                        })
        else:
            return Response(data={
                'status': 1,
                'message': ' L\' enregistrement des Entres et sorties est bien effectuée.'
            })




@api_view(['GET'])
def insertionParrainage(request):


    u = Parrainage.objects.values('id', 'parrain__id', 'filleul__id', 'date_heure_parrainage')

    print(u)
    for e1 in u:
        id = e1['id']
        parrain_id = e1['parrain__id']
        filleul_id = e1['filleul__id']
        date_heure_parrainage =e1['date_heure_parrainage']


        data = {
            'id':id,
            'parrain_id':parrain_id,
            'filleul_id':filleul_id,
            'date_heure_parrainage':date_heure_parrainage
        }

        url = 'http://5.196.224.234:8000/insertionDatabaseParrainnage/'

        datas = urllib.parse.urlencode(data)
        datas = datas.encode('utf-8')
        req = urllib.request.Request(url, datas)
        response = urllib.request.urlopen(req)
        the_page = response.read()

    return Response(data={
        'status': 0,
        'message': 'La synchronisation du parrainnage de la base de donnée locale sur la base de donnée distante est bien effective.'
    })





@api_view(['POST'])
def insertionDatabaseParrainnage(request):

    if request.method == "POST":

        id = request.data['id']
        parrain_id = request.data['parrain_id']
        filleul_id = request.data['filleul_id']
        date_heure_parrainage = request.data['date_heure_parrainage']

        userrrr = utilisateur2.objects.get(id=parrain_id)
        userrr1 = utilisateur2.objects.get(id=filleul_id)

        if len(userrrr)!=0 and len(userrr1)!=0:
            parrainage = Parrainage()

            parrainage.id = id
            parrainage.parrain_id = userrrr
            parrainage.filleul_id = userrr1
            parrainage.date_heure_parrainage = date_heure_parrainage

            parrainage.save()


            return Response(data={
                            'status': 0,
                            'message': ' L\' enregistrement du parrainage est bien effectuée.'
                        })
        else:
            return Response(data={
                'status': 1,
                'message': ' L\' enregistrement du parrainage est bien effectuée.'
            })



@api_view(['GET'])
def nombreAbonnees(request):


    nbAbonnees1 = Paiement.objects.all().values('idPaiement', 'date_debut', 'date_fin', 'idUser', 'nbseances_en_cours', 'nbseances_total', 'dateencours', 'date_autorisation', 'datebadge')
    nbAbonnees2 = utilisateur2.objects.all().values('id', 'prenom', 'nom', 'civilite', 'dateNaiss', 'lieuNaiss', 'adresse', 'ville', 'email', 'profession', 'prenom1', 'nom1', 'telephone1', 'prenom2', 'nom2', 'telephone2', 'telephone', 'photo', 'id_typeabonnement')
    tableau = []

    #print(datetime.now())
    #print(datetime.timedelta(days=30))

    for toto in nbAbonnees2:
        #print(toto)
        for toto1 in nbAbonnees1:
            #print(toto1)
            #if toto['id'] == toto1['idUser'] and toto1['datebadge'] >= datetime.now()- datetime.timedelta(days=30):
            if toto['id'] == toto1['idUser'] and toto1['datebadge'] != "None" and toto1['datebadge'] <= str(datetime.now() + timedelta(days=30)):

                data = {
                    "id": toto['id'],
                    "prenom": toto['prenom'],
                    "nom": toto['nom'],
                    "civilite": str(toto['civilite']),
                    "dateNaiss": str(toto['dateNaiss']),
                    "lieuNaiss": str(toto['lieuNaiss']),
                    "adresse": str(toto['adresse']),
                    "ville": str(toto['ville']),
                    "email": str(toto['email']),
                    "profession": str(toto['profession']),
                    "prenom1": str(toto['prenom1']),
                    "nom1": toto['nom1'],
                    "telephone1": toto['telephone1'],
                    "prenom2": str(toto['prenom2']),
                    "nom2": str(toto['nom2']),
                    "telephone2": str(toto['telephone2']),
                    "telephone": str(toto['telephone']),
                    "photo": str(toto['photo']),
                    "id_typeabonnement": toto['id_typeabonnement'],
                    "idPaiement": toto1['idPaiement'],
                    "date_debut": str(toto1['date_debut']),
                    "date_fin": str(toto1['date_fin']),
                    "nbseances_en_cours": toto1['nbseances_en_cours'],
                    "nbseances_total": toto1['nbseances_total'],
                    "dateencours": str(toto1['dateencours']),
                    "date_autorisation": str(toto1['date_autorisation']),
                    "datebadge": str(toto1['datebadge']),
                }
                tableau.append(data)

    return Response(
        data={
            'status': 0,
            'message': 'La  La liste des abonnées',
            'userss': list(tableau)
        })


@api_view(['GET'])
def nombreAbonnees30(request):
    if request.session.get('prenom') is None:
        print(' DANS DANS ')
        return render(request, 'login.html')
    else:

        employess = employers.objects.all()
        nbEmployess = employers.objects.count()

        abonnesss = Paiement.objects.all().values('idPaiement', 'date_debut', 'date_fin', 'idUser', 'idUser__prenom',
                                                  'idUser__nom',
                                                  'idUser__civilite', 'idUser__dateNaiss', 'idUser__lieuNaiss',
                                                  'idUser__adresse', 'idUser__ville', 'idUser__email',
                                                  'idUser__profession', 'idUser__prenom1', 'idUser__nom1',
                                                  'idUser__telephone1', 'idUser__prenom2', 'idUser__nom2',
                                                  'idUser__telephone2', 'idUser__telephone', 'idUser__photo',
                                                  'idUser__id_typeabonnement',
                                                  'nbseances_en_cours', 'nbseances_total', 'dateencours',
                                                  'date_autorisation', 'datebadge').filter(datebadge__lte=str(datetime.now() - timedelta(days=30)))
        abonnesss1 = Paiement.objects.all().values('idPaiement', 'date_debut', 'date_fin', 'idUser', 'idUser__prenom',
                                                  'idUser__nom',
                                                  'idUser__civilite', 'idUser__dateNaiss', 'idUser__lieuNaiss',
                                                  'idUser__adresse', 'idUser__ville', 'idUser__email',
                                                  'idUser__profession', 'idUser__prenom1', 'idUser__nom1',
                                                  'idUser__telephone1', 'idUser__prenom2', 'idUser__nom2',
                                                  'idUser__telephone2', 'idUser__telephone', 'idUser__photo',
                                                  'idUser__id_typeabonnement',
                                                  'nbseances_en_cours', 'nbseances_total', 'dateencours',
                                                  'date_autorisation', 'datebadge').filter(
            datebadge__lte=str(datetime.now() - timedelta(days=30))).count()

        return render(request, 'tables3.html', locals())


@api_view(['GET'])
def abonnes(request):
    if request.session.get('prenom') is None:
        print(' DANS DANS ')
        return render(request, 'login.html')
    else:
        abonnesss = Paiement.objects.all().values('idPaiement', 'date_debut', 'date_fin', 'idUser', 'idUser__prenom',
                                                  'idUser__nom',
                                                  'idUser__civilite', 'idUser__dateNaiss', 'idUser__lieuNaiss',
                                                  'idUser__adresse', 'idUser__ville', 'idUser__email',
                                                  'idUser__profession', 'idUser__prenom1', 'idUser__nom1',
                                                  'idUser__telephone1', 'idUser__prenom2', 'idUser__nom2',
                                                  'idUser__telephone2', 'idUser__telephone', 'idUser__photo',
                                                  'idUser__id_typeabonnement',
                                                  'nbseances_en_cours', 'nbseances_total', 'dateencours',
                                                  'date_autorisation', 'datebadge')


        return render(request, 'tables2.html', locals())






@api_view(['GET'])
def edit_user(request):

    if request.session.get('prenom') is None:
        print(' DANS DANS ')
        return render(request, 'login.html')
    else:

        test01 = request.GET["id"]

        us = request.session.get('id')
        print(" ID ID ID ID ID ID ID  ID ID ID ID ID ID ID ")
        print(" ID ID ID ID ID ID ID  ID ID ID ID ID ID ID ")
        print(" ID ID ID ID ID ID ID  ID ID ID ID ID ID ID ")
        print(" ID ID ID ID ID ID ID  ID ID ID ID ID ID ID ")
        print(us)
        print(us)
        print(us)

        utilisateur = utilisateur2.objects.get(id=test01)
        print(utilisateur)
        paiements = Paiement.objects.filter(idUser=us).values('idPaiement', 'date_debut', 'date_fin', 'idUser',
                                                    'nbseances_en_cours', 'nbseances_total', 'dateencours',
                                                    'date_autorisation', 'datebadge')
        print(paiements)


        paiement = {
            "idPaiement":paiements[0]['idPaiement'],
            "date_debut":paiements[0]['date_debut'],
            "date_fin":paiements[0]['date_fin'],
            "idUser":paiements[0]['idUser'],
            "nbseances_en_cours":paiements[0]['nbseances_en_cours'],
            "nbseances_total":paiements[0]['nbseances_total'],
            "dateencours":paiements[0]['dateencours']
        }

        request.session['id'] = test01
        return render(request, 'forms4.html', locals())



def parrainage(request):
    #tableau = []
    #stat = Parrainage.objects.all().values('id', 'parrain__id', 'parrain__prenom', 'parrain__nom', 'filleul__prenom', 'filleul__id', 'filleul__nom', 'date_heure_parrainage')
    #.annotate(entries=Count('parrain__id'))




    if request.session.get('prenom') is None:
        print(' DANS DANS ')
        return render(request, 'login.html')
    else:


        stat = Parrainage.objects.all().values('id', 'parrain__id', 'parrain__prenom', 'parrain__nom', 'filleul__prenom', 'filleul__id', 'filleul__nom', 'date_heure_parrainage')

        #stat = Parrainage.objects.annotate(parrain_count = Count('parrain__id')).values('parrain_count', 'filleul__id')

        # stat = Parrainage.objects.extra(
        #     select={
        #         'valeur': "SELECT *, COUNT(filleul_id) FROM users_parrainage GROUP BY parrain_id"
        #         #'SELECT users_parrainage.*, COUNT(filleul_id) FROM users_parrainage GROUP BY parrain_id AS Nombre FROM users_parrainage'
        #     }
        # )
        print(" stat ")
        print(" stat ")
        print(" stat ")
        print(stat)
        print(stat)
        print(stat)


        stat001 = Parrainage.objects.values('id', 'parrain__id', 'parrain__prenom', 'parrain__nom', 'filleul__prenom', 'filleul__id', 'filleul__nom', 'date_heure_parrainage').annotate(dcount=Count('filleul_id'))

        print(' stat001 ')
        print(' stat001 ')
        print(' stat001 ')
        print(stat001)
        print(stat001)
        print(stat001)





        # for valeur in stat:
        #     print(" valeur ")
        #     print(" valeur ")
        #     print(" valeur ")
        #     print(valeur)
        #     print(valeur['parrain__id'])
        #     valeur1 = Parrainage.objects.filter(parrain__id=valeur['parrain__id']).count()
        #     valeur001 = {
        #         "valeur1":valeur1
        #     }
        #     tableau.append(valeur001)
        #
        # print(" tableau ")
        # print(" tableau ")
        # print(tableau)
        return render(request, 'parrainage.html', locals())



def statistique4(request):
    if request.session.get('prenom') is None:
        print(' DANS DANS ')
        return render(request, 'login.html')
    else:
        return render(request, 'statisque4.html', locals())



def parrainage1(request):

    if request.session.get('prenom') is None:
        print(' DANS DANS ')
        return render(request, 'login.html')
    else:

        test = request.GET["id"]

        #test = request.session.get('id')
        print(" test ")
        print(" test ")
        print(" test ")
        print(test)
        valeur1 = Parrainage.objects.filter(parrain__id=test).count()



        # test = request.session.get('id')
        # print(" test ")
        # print(" test ")
        # print(" test ")
        # print(test)
        # valeur1 = Parrainage.objects.filter(parrain__id=test).count()
        stat = Parrainage.objects.all().values('id', 'parrain__id', 'parrain__prenom', 'parrain__nom', 'filleul__prenom', 'filleul__id', 'filleul__nom', 'date_heure_parrainage')
        test=""

        stat001 = Parrainage.objects.values('id', 'parrain__id', 'parrain__prenom', 'parrain__nom', 'filleul__prenom', 'filleul__id', 'filleul__nom', 'date_heure_parrainage').annotate(dcount=Count('parrain__id'))

        print(' stat001 ')
        print(' stat001 ')
        print(' stat001 ')
        print(stat001)
        print(stat001)
        print(stat001)
        return render(request, 'parrainage.html', locals())



def edit_user_valid(request):
    if request.session.get('prenom') is None:
        print(' DANS DANS ')
        return render(request, 'login.html')
    else:

        if request.POST["ok"] == "Modifier":
            test = request.session.get('id')
            print(test)
            idss = request.POST["id"]
            print(" idss idds idds idds")
            print(" idss idds idds idds")
            print(" idss idds idds idds")
            print(" idss idds idds idds")
            print(idss)
            user = utilisateur2.objects.get(id=test)

            user.nom=request.POST["nom"]
            user.prenom=request.POST["prenom"]
            user.civilite=request.POST["civilite"]
            user.dateNaiss=request.POST["dateNaiss"]
            user.email=request.POST["email"]
            user.profession=request.POST["profession"]

            user.telephone=request.POST["telephone"]
            user.telephone1=request.POST["telephone1"]
            user.prenom1=request.POST["prenom1"]
            user.nom1=request.POST["nom1"]
            user.telephone2 = request.POST["telephone2"]
            user.prenom2 = request.POST["prenom2"]
            user.nom2 = request.POST["nom2"]
            user.adresse = request.POST["adresse"]
            user.id_typeabonnement = request.POST["id_typeabonnement"]
            user.save()

            paiementss = Paiement.objects.get(idUser=test)

            paiementss.date_debut = request.POST["date_debut"]
            paiementss.date_fin = request.POST["date_fin"]
            paiementss.nbseances_en_cours = request.POST["nbseances_en_cours"]
            paiementss.nbseances_total = request.POST["nbseances_total"]
            paiementss.save()

            nbAbonnees = utilisateur2.objects.count()
            nbEssai = personne_essaie.objects.count()

            datedebut = datetime.now()

            datedebut1 = datedebut.strftime("%Y-%m-%d")

            datefin = datetime.now() - timedelta(days=30)
            datefin1 = datefin.strftime("%Y-%m-%d")

            print(' datefin1 ')
            print(' datefin1 ')
            print(datefin1)
            print('datedebut')
            print('datedebut')
            print('datedebut')
            print(datedebut1)

            print(' datetime.now()-timedelta(days=30) ')
            print(' datetime.now()-timedelta(days=30) ')
            print(' datetime.now()-timedelta(days=30) ')
            print(datetime.now() - timedelta(days=30))
            print(datetime.now() - timedelta(days=30))
            print(datetime.now() - timedelta(days=30))

            # nouveauxInscrits = Paiement.objects.filter(date_debut__gte=str(datetime.now() - timedelta(days=30))).count()
            nouveauxInscrits = Paiement.objects.filter(date_debut__range=(datefin1, datedebut1)).count()
            nouveauxInscrits1 = Paiement.objects.filter(date_debut__range=(datefin1, datedebut1)).values('idPaiement',
                                                                                                         'date_debut',
                                                                                                         'date_fin',
                                                                                                         'idUser',
                                                                                                         'idUser__prenom',
                                                                                                         'idUser__nom',
                                                                                                         'idUser__civilite',
                                                                                                         'idUser__dateNaiss',
                                                                                                         'idUser__lieuNaiss',
                                                                                                         'idUser__adresse',
                                                                                                         'idUser__ville',
                                                                                                         'idUser__email',
                                                                                                         'idUser__profession',
                                                                                                         'idUser__prenom1',
                                                                                                         'idUser__nom1',
                                                                                                         'idUser__telephone1',
                                                                                                         'idUser__prenom2',
                                                                                                         'idUser__nom2',
                                                                                                         'idUser__telephone2',
                                                                                                         'idUser__telephone',
                                                                                                         'idUser__photo',
                                                                                                         'idUser__id_typeabonnement',
                                                                                                         'nbseances_en_cours',
                                                                                                         'nbseances_total',
                                                                                                         'dateencours',
                                                                                                         'date_autorisation',
                                                                                                         'datebadge')

            abonnesss = Paiement.objects.all().values('idPaiement', 'date_debut', 'date_fin', 'idUser', 'idUser__prenom',
                                                      'idUser__nom',
                                                      'idUser__civilite', 'idUser__dateNaiss', 'idUser__lieuNaiss',
                                                      'idUser__adresse', 'idUser__ville', 'idUser__email',
                                                      'idUser__profession', 'idUser__prenom1', 'idUser__nom1',
                                                      'idUser__telephone1', 'idUser__prenom2', 'idUser__nom2',
                                                      'idUser__telephone2', 'idUser__telephone', 'idUser__photo',
                                                      'idUser__id_typeabonnement',
                                                      'nbseances_en_cours', 'nbseances_total', 'dateencours',
                                                      'date_autorisation', 'datebadge')
            print(" abonnesss ")
            print(abonnesss)

            abonnesss11 = Paiement.objects.all().values('idPaiement', 'date_debut', 'date_fin', 'idUser', 'idUser__prenom',
                                                        'idUser__nom',
                                                        'idUser__civilite', 'idUser__dateNaiss', 'idUser__lieuNaiss',
                                                        'idUser__adresse', 'idUser__ville', 'idUser__email',
                                                        'idUser__profession', 'idUser__prenom1', 'idUser__nom1',
                                                        'idUser__telephone1', 'idUser__prenom2', 'idUser__nom2',
                                                        'idUser__telephone2', 'idUser__telephone', 'idUser__photo',
                                                        'idUser__id_typeabonnement',
                                                        'nbseances_en_cours', 'nbseances_total', 'dateencours',
                                                        'date_autorisation', 'datebadge').filter(
                datebadge__lte=str(datetime.now() - timedelta(days=30)))

            abonnesss22 = Paiement.objects.all().values('idPaiement', 'date_debut', 'date_fin', 'idUser', 'idUser__prenom',
                                                        'idUser__nom',
                                                        'idUser__civilite', 'idUser__dateNaiss', 'idUser__lieuNaiss',
                                                        'idUser__adresse', 'idUser__ville', 'idUser__email',
                                                        'idUser__profession', 'idUser__prenom1', 'idUser__nom1',
                                                        'idUser__telephone1', 'idUser__prenom2', 'idUser__nom2',
                                                        'idUser__telephone2', 'idUser__telephone', 'idUser__photo',
                                                        'idUser__id_typeabonnement',
                                                        'nbseances_en_cours', 'nbseances_total', 'dateencours',
                                                        'date_autorisation', 'datebadge').filter(
                datebadge__lte=str(datetime.now() - timedelta(days=30))).count()

            return render(request, 'dashboard.html', locals())


        else:
            if request.POST['ok'] == "Supprimer":
                print(" Suprresion ")
                print(" Suprresion ")
                print(" Suprresion ")
                test = request.session.get('id')

                paiementssss = Paiement.objects.get(idUser=test)
                user = utilisateur2.objects.get(id=test)
                paiementssss.delete()
                user.delete()

                nbAbonnees = utilisateur2.objects.count()
                nbEssai = personne_essaie.objects.count()

                abonnesss = Paiement.objects.all().values('idPaiement', 'date_debut', 'date_fin', 'idUser',
                                                          'idUser__prenom',
                                                          'idUser__nom',
                                                          'idUser__civilite', 'idUser__dateNaiss', 'idUser__lieuNaiss',
                                                          'idUser__adresse', 'idUser__ville', 'idUser__email',
                                                          'idUser__profession', 'idUser__prenom1', 'idUser__nom1',
                                                          'idUser__telephone1', 'idUser__prenom2', 'idUser__nom2',
                                                          'idUser__telephone2', 'idUser__telephone', 'idUser__photo',
                                                          'idUser__id_typeabonnement',
                                                          'nbseances_en_cours', 'nbseances_total', 'dateencours',
                                                          'date_autorisation', 'datebadge')
                print(" abonnesss ")
                print(abonnesss)

                abonnesss11 = Paiement.objects.all().values('idPaiement', 'date_debut', 'date_fin', 'idUser',
                                                            'idUser__prenom',
                                                            'idUser__nom',
                                                            'idUser__civilite', 'idUser__dateNaiss', 'idUser__lieuNaiss',
                                                            'idUser__adresse', 'idUser__ville', 'idUser__email',
                                                            'idUser__profession', 'idUser__prenom1', 'idUser__nom1',
                                                            'idUser__telephone1', 'idUser__prenom2', 'idUser__nom2',
                                                            'idUser__telephone2', 'idUser__telephone', 'idUser__photo',
                                                            'idUser__id_typeabonnement',
                                                            'nbseances_en_cours', 'nbseances_total', 'dateencours',
                                                            'date_autorisation', 'datebadge').filter(
                    datebadge__lte=str(datetime.now() - timedelta(days=30)))

                abonnesss22 = Paiement.objects.all().values('idPaiement', 'date_debut', 'date_fin', 'idUser',
                                                            'idUser__prenom',
                                                            'idUser__nom',
                                                            'idUser__civilite', 'idUser__dateNaiss', 'idUser__lieuNaiss',
                                                            'idUser__adresse', 'idUser__ville', 'idUser__email',
                                                            'idUser__profession', 'idUser__prenom1', 'idUser__nom1',
                                                            'idUser__telephone1', 'idUser__prenom2', 'idUser__nom2',
                                                            'idUser__telephone2', 'idUser__telephone', 'idUser__photo',
                                                            'idUser__id_typeabonnement',
                                                            'nbseances_en_cours', 'nbseances_total', 'dateencours',
                                                            'date_autorisation', 'datebadge').filter(
                    datebadge__lte=str(datetime.now() - timedelta(days=30))).count()

                return render(request, 'dashboard.html', locals())

            else:
                print(" Suprresion 1")
                print(" Suprresion 1")
                print(" Suprresion 1")

                nbAbonnees = utilisateur2.objects.count()
                nbEssai = personne_essaie.objects.count()

                datedebut = datetime.now()

                datedebut1 = datedebut.strftime("%Y-%m-%d")

                datefin = datetime.now() - timedelta(days=30)
                datefin1 = datefin.strftime("%Y-%m-%d")

                print(' datefin1 ')
                print(' datefin1 ')
                print(datefin1)
                print('datedebut')
                print('datedebut')
                print('datedebut')
                print(datedebut1)

                print(' datetime.now()-timedelta(days=30) ')
                print(' datetime.now()-timedelta(days=30) ')
                print(' datetime.now()-timedelta(days=30) ')
                print(datetime.now() - timedelta(days=30))
                print(datetime.now() - timedelta(days=30))
                print(datetime.now() - timedelta(days=30))

                # nouveauxInscrits = Paiement.objects.filter(date_debut__gte=str(datetime.now() - timedelta(days=30))).count()
                nouveauxInscrits = Paiement.objects.filter(date_debut__range=(datefin1, datedebut1)).count()
                nouveauxInscrits1 = Paiement.objects.filter(date_debut__range=(datefin1, datedebut1)).values('idPaiement',
                                                                                                             'date_debut',
                                                                                                             'date_fin',
                                                                                                             'idUser',
                                                                                                             'idUser__prenom',
                                                                                                             'idUser__nom',
                                                                                                             'idUser__civilite',
                                                                                                             'idUser__dateNaiss',
                                                                                                             'idUser__lieuNaiss',
                                                                                                             'idUser__adresse',
                                                                                                             'idUser__ville',
                                                                                                             'idUser__email',
                                                                                                             'idUser__profession',
                                                                                                             'idUser__prenom1',
                                                                                                             'idUser__nom1',
                                                                                                             'idUser__telephone1',
                                                                                                             'idUser__prenom2',
                                                                                                             'idUser__nom2',
                                                                                                             'idUser__telephone2',
                                                                                                             'idUser__telephone',
                                                                                                             'idUser__photo',
                                                                                                             'idUser__id_typeabonnement',
                                                                                                             'nbseances_en_cours',
                                                                                                             'nbseances_total',
                                                                                                             'dateencours',
                                                                                                             'date_autorisation',
                                                                                                             'datebadge')

                abonnesss = Paiement.objects.all().values('idPaiement', 'date_debut', 'date_fin', 'idUser',
                                                          'idUser__prenom',
                                                          'idUser__nom',
                                                          'idUser__civilite', 'idUser__dateNaiss', 'idUser__lieuNaiss',
                                                          'idUser__adresse', 'idUser__ville', 'idUser__email',
                                                          'idUser__profession', 'idUser__prenom1', 'idUser__nom1',
                                                          'idUser__telephone1', 'idUser__prenom2', 'idUser__nom2',
                                                          'idUser__telephone2', 'idUser__telephone', 'idUser__photo',
                                                          'idUser__id_typeabonnement',
                                                          'nbseances_en_cours', 'nbseances_total', 'dateencours',
                                                          'date_autorisation', 'datebadge')
                print(" abonnesss ")
                print(abonnesss)

                abonnesss11 = Paiement.objects.all().values('idPaiement', 'date_debut', 'date_fin', 'idUser',
                                                            'idUser__prenom',
                                                            'idUser__nom',
                                                            'idUser__civilite', 'idUser__dateNaiss', 'idUser__lieuNaiss',
                                                            'idUser__adresse', 'idUser__ville', 'idUser__email',
                                                            'idUser__profession', 'idUser__prenom1', 'idUser__nom1',
                                                            'idUser__telephone1', 'idUser__prenom2', 'idUser__nom2',
                                                            'idUser__telephone2', 'idUser__telephone', 'idUser__photo',
                                                            'idUser__id_typeabonnement',
                                                            'nbseances_en_cours', 'nbseances_total', 'dateencours',
                                                            'date_autorisation', 'datebadge').filter(
                    datebadge__range=(datefin1,datedebut1))

                abonnesss22 = Paiement.objects.all().values('idPaiement', 'date_debut', 'date_fin', 'idUser',
                                                            'idUser__prenom',
                                                            'idUser__nom',
                                                            'idUser__civilite', 'idUser__dateNaiss', 'idUser__lieuNaiss',
                                                            'idUser__adresse', 'idUser__ville', 'idUser__email',
                                                            'idUser__profession', 'idUser__prenom1', 'idUser__nom1',
                                                            'idUser__telephone1', 'idUser__prenom2', 'idUser__nom2',
                                                            'idUser__telephone2', 'idUser__telephone', 'idUser__photo',
                                                            'idUser__id_typeabonnement',
                                                            'nbseances_en_cours', 'nbseances_total', 'dateencours',
                                                            'date_autorisation', 'datebadge').filter(
                    datebadge__range=(datefin1,datedebut1)).count()

                return render(request, 'dashboard.html', locals())


