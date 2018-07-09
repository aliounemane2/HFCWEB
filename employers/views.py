from django.shortcuts import render
from rest_framework.decorators import api_view
from employers.serializers import *
from employers.models import *
from rest_framework.response import Response
from rest_framework import status
import urllib.parse
import urllib.request
import ssl
from django.http import HttpResponse
import base64
from django.core.files.base import ContentFile
from django.conf import settings
import urllib.request
import os
from django.core.files.storage import default_storage
from datetime import datetime, timedelta
import time
from users.models import utilisateur2, Paiement, Type_Abonnement
from essaies.models import *
from PIL import Image
from io import BytesIO
import json
#import cStringIO
from io import StringIO










@api_view(['GET'])
def insertionEmployers(request):

    u0 = employers.objects.values('id', 'civilte', 'prenom', 'nom', 'profession', 'dateNaiss', 'carte_didentite_nationale',
                                 'telephone', 'email', 'adresse', 'idcarte', 'prenom1', 'nom1', 'telephone1', 'prenom2', 'nom2',
                                 'telephone2', 'photo', 'photo2')
    print(u0)
    for e1 in u0:

        id = e1['id']
        civilite = e1['civilte']
        prenom = e1['prenom']
        nom = e1['nom']
        profession = e1['profession']
        dateNaiss = e1['dateNaiss']
        carte_didentite_nationale = e1['carte_didentite_nationale']
        telephone = e1['telephone']
        email = e1['email']
        adresse = e1['adresse']
        idcarte = e1['idcarte']
        prenom1 = e1['prenom1']
        nom1 = e1['nom1']
        telephone1 = e1['telephone1']
        prenom2 = e1['prenom2']
        nom2 = e1['nom2']
        telephone2 = e1['telephone2']
        photo = e1['photo']
        photo2 = e1['photo2']

        data = {
            'id':id,
            'civilite':civilite,
            'prenom':prenom,
            'nom':nom,
            'profession': profession,
            'dateNaiss': dateNaiss,
            'carte_didentite_nationale': carte_didentite_nationale,
            'telephone': telephone,
            'email': email,
            'adresse': adresse,
            'idcarte': idcarte,
            'prenom1': prenom1,
            'nom1': nom1,
            'telephone1': telephone1,
            'prenom2': prenom2,
            'nom2': nom2,
            'telephone2': telephone2,
            'photo': photo,
            'photo2': photo2
        }


        url = 'http://5.196.224.234:8000/insertionEmployersDatabase/'

        datass = urllib.parse.urlencode(data)
        datass = datass.encode('utf-8')
        reqs = urllib.request.Request(url, datass)
        response = urllib.request.urlopen(reqs)
        the_page = response.read()


    return Response(data={
                    'status': 0,
                    'message': 'La synchronisation de la base de donnée locale sur la base distante est bien effectuée.'
                })






@api_view(['POST'])
def insertionEmployersDatabase(request):

    if request.method == "POST":


        ids = request.data['id']
        civilite = request.data['civilite']
        prenom = request.data['prenom']
        nom = request.data['nom']
        dateNaiss = request.data['dateNaiss']
        adresse = request.data['adresse']
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
        photo = request.data['photo']
        photo2 = request.data['photo2']
        carte_didentite_nationale = request.data['carte_didentite_nationale']

        employersss = employers()
        employersss.id = ids
        employersss.civilte = civilite
        employersss.prenom = prenom
        employersss.nom = nom
        employersss.profession = profession
        employersss.dateNaiss = dateNaiss
        employersss.carte_didentite_nationale	 = 	carte_didentite_nationale
        employersss.telephone = telephone
        employersss.email = email
        employersss.adresse = adresse
        employersss.idcarte = idcarte
        employersss.prenom1 = prenom1
        employersss.nom1 = nom1
        employersss.telephone1 = telephone1
        employersss.prenom2 = prenom2
        employersss.nom2 = nom2
        employersss.telephone2 = telephone2
        employersss.photo = photo
        employersss.photo2 = photo2
        employersss.save()

        return Response(data={
                        'status': 0,
                        'message': ' L\' enregistrement est bien effectuée. '
                    })






@api_view(['GET'])
def insertionPointage(request):

    #u = User.objects.get(telephone=telephone)

    u0 = pointage.objects.values('id', 'idUser', 'date_et_heures')
    print(u0)
    for e1 in u0:

        id = e1['id']
        idUser = e1['idUser']
        date_et_heures = e1['date_et_heures']

        data = {
            'id':id,
            'idUser':idUser,
            'date_et_heures':date_et_heures
        }

        url = 'http://5.196.224.234:8000/insertionPointageDatabase/'

        datas = urllib.parse.urlencode(data)
        datas = datas.encode('utf-8')

        req = urllib.request.Request(url, datas)
        response = urllib.request.urlopen(req)
        the_page = response.read()

    return Response(data={
                    'status': 0,
                    'message': 'L enregistrement de la base de donnée locale sur la base la base distante est effective.'
                })





@api_view(['POST'])
def insertionPointageDatabase(request):

    if request.method == "POST":


        ids = request.data['id']
        idUser = request.data['idUser']
        date_et_heures = request.data['date_et_heures']

        userrrr = utilisateur2.objects.get(id=idUser)
        if len(userrrr)!= 0:
            pointagess = pointage()
            pointagess.id = ids
            pointagess.idUser = userrrr
            pointagess.date_et_heures = date_et_heures
            pointagess.save()

            return Response(data={
                            'status': 0,
                            'message': ' L\' enregistrement est bien effectuée. '
                        })
        else:
            return Response(data={
                'status': 0,
                'message': ' L\' enregistrement est bien effectuée. '
            })





def insertionEmployerss(request):

    # ids = request.data['id']
    #### if request.method == "POST":

    if request.session.get('prenom') is None:

        print(' DANS DANS ')
        return render(request, 'login.html')

    else:

        prenom = request.POST["prenom"]
        nom = request.POST["nom"]
        dateNaiss = request.POST["dateNaiss"]
        adresse = request.POST["adresse"]
        email = request.POST["email"]
        profession = request.POST["profession"]
        prenom1 = request.POST["prenom1"]
        nom1 = request.POST["nom1"]
        telephone1 = request.POST["telephone1"]
        prenom2 = request.POST["prenom2"]
        nom2 = request.POST["nom2"]
        telephone2 = request.POST["telephone2"]
        #idcarte = request.POST["idcarte"]
        telephone = request.POST["telephone"]
        #photo = request.POST["photo"]
        carte_didentite_nationale = request.POST["carte_didentite_nationale"]
        civilite = request.POST["civilite"]

        print(" request.FILES['photo'] ")
        print(" request.FILES['photo'] ")
        print(" request.FILES['photo'] ")
        print(request.FILES['photo'])
        image = request.FILES['photo']


        employersss = employers()

        request.session['prenom'] = prenom
        request.session['nom'] = nom
        request.session['dateNaiss'] = dateNaiss
        request.session['adresse'] = adresse
        request.session['email'] = email
        request.session['profession'] = profession
        request.session['prenom1'] = prenom1
        request.session['nom1'] = nom1
        request.session['telephone1'] = telephone1
        request.session['prenom2'] = prenom2
        request.session['nom2'] = nom2
        request.session['telephone2'] = telephone2
        request.session['telephone'] = telephone
        request.session['carte_didentite_nationale'] = carte_didentite_nationale
        request.session['civilite'] = civilite
        #request.session['photo'] = image


        if request.POST["email"] == "":
            email = ""



        if employers.objects.filter(email=email).count() > 0:

            print(' employers.objects.filter(email=email).count() ')
            print(' employers.objects.filter(email=email).count() ')
            request.session['prenom'] = prenom
            request.session['nom'] = nom
            request.session['dateNaiss'] = dateNaiss
            request.session['adresse'] = adresse
            request.session['email'] = email
            request.session['profession'] = profession
            request.session['prenom1'] = prenom1
            request.session['nom1'] = nom1
            request.session['telephone1'] = telephone1
            request.session['prenom2'] = prenom2
            request.session['nom2'] = nom2
            request.session['telephone2'] = telephone2
            request.session['telephone'] = telephone
            request.session['carte_didentite_nationale'] = carte_didentite_nationale
            request.session['civilite'] = civilite
            #request.session['photo'] = image

            print(employers.objects.filter(email=email).count())
            message3="Le mail existe déjà en base. Veuillez le changer svp."
            return render(request, 'forms.html', locals())

        elif employers.objects.filter(telephone=telephone).count()>0:
            request.session['prenom'] = prenom
            request.session['nom'] = nom
            request.session['dateNaiss'] = dateNaiss
            request.session['adresse'] = adresse
            request.session['email'] = email
            request.session['profession'] = profession
            request.session['prenom1'] = prenom1
            request.session['nom1'] = nom1
            request.session['telephone1'] = telephone1
            request.session['prenom2'] = prenom2
            request.session['nom2'] = nom2
            request.session['telephone2'] = telephone2
            request.session['telephone'] = telephone
            request.session['carte_didentite_nationale'] = carte_didentite_nationale
            request.session['civilite'] = civilite
            #request.session['photo'] = image

            message2="Ce numéro de téléphone existe déjà en base. Veuillez le changer svp."
            return render(request, 'forms.html', locals())

        elif employers.objects.filter(carte_didentite_nationale=carte_didentite_nationale).count()>0:
            request.session['prenom'] = prenom
            request.session['nom'] = nom
            request.session['dateNaiss'] = dateNaiss
            request.session['adresse'] = adresse
            request.session['email'] = email
            request.session['profession'] = profession
            request.session['prenom1'] = prenom1
            request.session['nom1'] = nom1
            request.session['telephone1'] = telephone1
            request.session['prenom2'] = prenom2
            request.session['nom2'] = nom2
            request.session['telephone2'] = telephone2
            request.session['telephone'] = telephone
            request.session['carte_didentite_nationale'] = carte_didentite_nationale
            request.session['civilite'] = civilite
            #request.session['photo'] = image

            message1="Ce CIN existe déjà en base. Veuillez le changer svp."
            return render(request, 'forms.html', locals())

        else:





            # employersss.id = ids
            employersss.civilte = civilite
            employersss.prenom = prenom
            employersss.nom = nom
            employersss.profession = profession
            employersss.dateNaiss = dateNaiss
            employersss.carte_didentite_nationale=carte_didentite_nationale
            employersss.telephone = telephone
            employersss.email = email
            employersss.adresse = adresse
            #employersss.idcarte = idcarte
            employersss.prenom1 = prenom1
            employersss.nom1 = nom1
            employersss.telephone1 = telephone1
            employersss.prenom2 = prenom2
            employersss.nom2 = nom2
            employersss.telephone2 = telephone2
            employersss.photo2 = image

            print(" employers.photo ===== >>>>>> ")
            print(" employers.photo ===== >>>>>> ")
            print(" employers.photo ===== >>>>>> ")
            print(" employers.photo ===== >>>>>> ")
            print(" employers.photo ===== >>>>>> ")
            print(employers.photo2)
            print(employers.photo2)
            print(employers.photo2)

            ################################# fullfilename = os.path.join('media/employers/', photo)

            employersss.save()

            #with open("media/employers/"+employersss.photo+"", "rb") as imageFile:
            #    str = base64.b64encode(imageFile.read())
            #    print (str)


            ##employersss.save()
            #encoded_string = ''
            # with open(str("employers/"+employersss.photo), 'rb') as img_f:
            #with open("media/employers/"+employersss.photo+"", 'rb') as img_f:
              #  encoded_string = base64.b64encode(img_f.read())
               # print(" encoded_string 11111")
               # print(" encoded_string 11111")
               # print(" encoded_string 11111")
               # print(encoded_string)
                #print(" encoded_string 11111")
                #print(" encoded_string 11111")
                #print(" encoded_string 11111")
            #return 'data:image/%s;base64,%s' % (format, encoded_string)


            print("employersss.photo")
            print("employersss.photo")
            print("employersss.photo")



            #fullfilename = os.path.join('media/employers/', photo)
            #print(fullfilename)

            #path = default_storage.save('employers/', str(photo))
            print("path")
            print("path")
            print("path")
            #print(path)

            ################# print(settings.MEDIA_ROOT)
            ################# print(settings.MEDIA_ROOT)
            ################# save_path = os.path.join(settings.MEDIA_ROOT, 'employers', request.POST["photo"])

            #os.rename(settings.MEDIA_ROOT+"/employers", settings.MEDIA_ROOT+"/employers/"+request.POST["photo"])
            ################# default_storage.save(save_path, request.POST["photo"])

            #wp = urllib.request.urlopen("http://127.0.0.1:8000/media/employers/"+str(employersss.photo))
            #pw = base64.b64encode(wp.read())
            #employersss.photo=pw
            #employersss.save()


            print("pw")
            print("pw")
            print("pw")
            #print(pw)
            #print(pw)
            #print(pw)


            print(" COOOOOLLLLL ")
            print(" COOOOOLLLLL ")
            print(" COOOOOLLLLL ")
            print(" COOOOOLLLLL ")
            print(" COOOOOLLLLL ")
            print(" COOOOOLLLLL ")
            print(" COOOOOLLLLL ")
            print(" COOOOOLLLLL ")
            ### with open(photo, "rb") as image_file:

            ####### encoded_string = base64.b64encode(photo)
            # = base64.b64encode(photo)
            #print(encoded_string)

            ### data_bytes = data.encode("utf-8")
            #### base64.b64encode(data_byte)

            print("encoded_string")
            print("encoded_string")
            print("encoded_string")
            #print(encoded_string)

            # employersss.photo = photo

            nbAbonnees = utilisateur2.objects.count()
            nbEssai = personne_essaie.objects.count()

            datedebut = datetime.now()

            datedebut1 = datedebut.strftime("%Y-%m-%d")

            datefin = datetime.now()-timedelta(days=30)
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
            print(datetime.now()-timedelta(days=30))
            print(datetime.now()-timedelta(days=30))
            print(datetime.now()-timedelta(days=30))


            #nouveauxInscrits = Paiement.objects.filter(date_debut__gte=str(datetime.now() - timedelta(days=30))).count()
            nouveauxInscrits = Paiement.objects.filter(date_debut__range=(datefin1,datedebut1)).count()
            nouveauxInscrits1 = Paiement.objects.filter(date_debut__range=(datefin1,datedebut1)).values('idPaiement', 'date_debut', 'date_fin', 'idUser', 'idUser__prenom',
                                                      'idUser__nom',
                                                      'idUser__civilite', 'idUser__dateNaiss', 'idUser__lieuNaiss',
                                                      'idUser__adresse', 'idUser__ville', 'idUser__email',
                                                      'idUser__profession', 'idUser__prenom1', 'idUser__nom1',
                                                      'idUser__telephone1', 'idUser__prenom2', 'idUser__nom2',
                                                      'idUser__telephone2', 'idUser__telephone', 'idUser__photo',
                                                      'idUser__id_typeabonnement',
                                                      'nbseances_en_cours', 'nbseances_total', 'dateencours',
                                                      'date_autorisation', 'datebadge')

            nbAbonnees1 = Paiement.objects.all().values('idPaiement', 'date_debut', 'date_fin', 'idUser',
                                                        'nbseances_en_cours', 'nbseances_total', 'dateencours',
                                                        'date_autorisation', 'datebadge')

            nbAbonnees2 = utilisateur2.objects.all().values('id', 'prenom', 'nom', 'civilite', 'dateNaiss', 'lieuNaiss',
                                                            'adresse', 'ville', 'email', 'profession', 'prenom1', 'nom1',
                                                            'telephone1', 'prenom2', 'nom2', 'telephone2', 'telephone',
                                                            'photo', 'id_typeabonnement')
            tableau = []

            comparer = str(datetime.now() - timedelta(days=30))
            print(" LA DATE DE COMPARAISON ")
            print(" LA DATE DE COMPARAISON ")
            print(" LA DATE DE COMPARAISON ")
            print(" LA DATE DE COMPARAISON ")
            print(" LA DATE DE COMPARAISON ")
            print(" LA DATE DE COMPARAISON ")
            print(comparer)
            print(comparer)
            print(comparer[:10])
            comparer0 = comparer[:10]

            # comparer0 = comparer[:10]

            formatter_string = "%Y-%m-%d"
            comparer1 = datetime.strptime(comparer0, formatter_string)

            print(" LLLLLLLLLLLLLLLLLLLLLLLLLL ")
            print(" LLLLLLLLLLLLLLLLLLLLLLLLLL ")
            print(" LLLLLLLLLLLLLLLLLLLLLLLLLL ")
            print(" LLLLLLLLLLLLLLLLLLLLLLLLLL ")
            print(" LLLLLLLLLLLLLLLLLLLLLLLLLL ")

            # for toto in nbAbonnees2:
            #     for toto1 in nbAbonnees1:
            #         print(" BAKHNA ")
            #         print(" BAKHNA ")
            #         print(" BAKHNA ")
            #         print(" BAKHNA ")
            #         print(toto1['datebadge'])
            #         print(toto1['datebadge'][:10])
            #         print(toto1['datebadge'])
            #         toto222 = datetime.strptime(toto1['datebadge'][:10], formatter_string)
            #         print(" toto222 ")
            #         print(" toto222 ")
            #         print(" toto222 ")
            #         print(" toto222 ")
            #         print(toto222)
            #         print(toto222)
            #         print(toto222)
            #
            #         # if toto['id'] == toto1['idUser'] and toto1['datebadge'] != "None" and toto1['datebadge'] <= comparer1:
            #         if toto['id'] == toto1['idUser'] and toto1['datebadge'] != "None" and toto1[
            #             'datebadge'] != "NULL" and datetime.strptime(str(toto1['datebadge']),
            #                                                          formatter_string) <= comparer1:
            #             data01 = {
            #                 "id": toto['id'],
            #                 "prenom": toto['prenom'],
            #                 "nom": toto['nom'],
            #                 "civilite": str(toto['civilite']),
            #                 "dateNaiss": str(toto['dateNaiss']),
            #                 "lieuNaiss": str(toto['lieuNaiss']),
            #                 "adresse": str(toto['adresse']),
            #                 "ville": str(toto['ville']),
            #                 "email": str(toto['email']),
            #                 "profession": str(toto['profession']),
            #                 "prenom1": str(toto['prenom1']),
            #                 "nom1": toto['nom1'],
            #                 "telephone1": toto['telephone1'],
            #                 "prenom2": str(toto['prenom2']),
            #                 "nom2": str(toto['nom2']),
            #                 "telephone2": str(toto['telephone2']),
            #                 "telephone": str(toto['telephone']),
            #                 "photo": str(toto['photo']),
            #                 "id_typeabonnement": toto['id_typeabonnement'],
            #                 "idPaiement": toto1['idPaiement'],
            #                 "date_debut": str(toto1['date_debut']),
            #                 "date_fin": str(toto1['date_fin']),
            #                 "nbseances_en_cours": toto1['nbseances_en_cours'],
            #                 "nbseances_total": toto1['nbseances_total'],
            #                 "dateencours": str(toto1['dateencours']),
            #                 "date_autorisation": str(toto1['date_autorisation']),
            #                 "datebadge": str(toto1['datebadge']),
            #             }
            #             tableau.append(data01)
            #             taille = len(tableau)

        employess = employers.objects.all()
        nbEmployess = employers.objects.count()

        return render(request, 'dashboard.html', locals())


    #return render(request, 'blank.html', locals())

def updateEmployers(request):
    if request.session.get('prenom') is None:
        print(' DANS DANS ')
        return render(request, 'login.html')
    else:

        # ids = request.data['id']
        civilite = request.data['civilite']
        prenom = request.data['prenom']
        nom = request.data['nom']
        dateNaiss = request.data['dateNaiss']
        adresse = request.data['adresse']
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
        photo2 = request.data['photo2']
        carte_didentite_nationale = request.data['carte_didentite_nationale']


        employersss = employers.objects.get(telephone=telephone)

        if employersss is not None:

        # employersss.id = ids
            employersss.civilte = civilite
            employersss.prenom = prenom
            employersss.nom = nom
            employersss.profession = profession
            employersss.dateNaiss = dateNaiss
            employersss.carte_didentite_nationale=carte_didentite_nationale
            employersss.telephone = telephone
            employersss.email = email
            employersss.adresse = adresse
            employersss.idcarte = idcarte
            employersss.prenom1 = prenom1
            employersss.nom1 = nom1
            employersss.telephone1 = telephone1
            employersss.prenom2 = prenom2
            employersss.nom2 = nom2
            employersss.telephone2 = telephone2
            employersss.photo2 = photo2
            employersss.save()

            return render(request, 'blank.html', locals())
        return render(request, 'blank.html', locals())


def deleteEmployers(request):
    if request.session.get('prenom') is None:
        print(' DANS DANS ')
        return render(request, 'login.html')
    else:
        ids = request.data['id']
        telephone = request.data['telephone']

        employersss = employers.objects.get(id=ids)

        if employersss is not None:

            employersss.delete()

            return render(request, 'blank.html', locals())
        return render(request, 'blank.html', locals())



def forms(request):
    if request.session.get('prenom') is None:
        print(' DANS DANS ')
        return render(request, 'login.html')
    else:
        employess = employers.objects.all()
        nbEmployess = employers.objects.count()
        return render(request, 'forms.html', locals())


def employersall(request):

    #employerss = employers.objects.all()


    if request.session.get('prenom') is None:
        print(' DANS DANS ')
        return render(request, 'login.html')
    else:

        tableau = []

        employerss = employers.objects.all()

        employerss11 = employers.objects.count()
        print(employerss11)
        print(employerss)
        for employersss in employerss:


            print(employersss)
            print(employersss)
            emppp = employers.objects.get(telephone=employersss)
            prenommm = emppp.prenom
            nommm = emppp.nom
            telephonee = emppp.telephone
            emaill = emppp.email
            idsss = emppp.id

            pointagess = pointage.objects.filter(idUser=idsss).last()
            print(' pointagess ')
            print(' pointagess ')
            print(' pointagess ')
            print(pointagess)

            if pointagess is None or pointagess=="None":
                pointagess =""

            data = {
                "id":idsss,
                "prenom":prenommm,
                "nom":nommm,
                "telephone":telephonee,
                "email":emaill,
                "pointage": pointagess
            }
            tableau.append(data)

            #pointage = pointage.objects.get(id=7)
            print(' emppp.prenom ')
            print(' emppp.prenom ')
            #print(emppp.prenom)
            print(' emppp.nom ')
            print(' emppp.nom ')
            #print(emppp.nom)
        print(" tableau ")
        print(" tableau ")
        print(" tableau ")
        print(tableau)
        print(tableau)


        print(' employerss ')
        print(' employerss ')
        print(employerss)
        us = request.session.get('id')

        #request.session['id'] = employerss.id
        return render(request, 'tables4.html', locals())




def employersalls(request):

    if request.session.get('prenom') is None:
        print(' DANS DANS ')
        return render(request, 'login.html')
    else:

        employerss = employers.objects.all()
        #employerss = pointage.objects.values('idUser__nom', 'idUser__prenom', 'idUser__email')

        #employerss = employers.objects.all()
        us = request.session.get('id')
        # request.session['id'] = employerss.id


        tableau = []

        employerss = employers.objects.all()

        employerss11 = employers.objects.count()
        print(employerss11)
        print(employerss)
        for employersss in employerss:


            print(employersss)
            print(employersss)
            emppp = employers.objects.get(telephone=employersss)
            prenommm = emppp.prenom
            nommm = emppp.nom
            telephonee = emppp.telephone
            emaill = emppp.email
            idsss = emppp.id

            pointagess = pointage.objects.filter(idUser=idsss).last()

            if pointagess is None or pointagess=="None":
                pointagess =""
            print(' pointagess ')
            print(' pointagess ')
            print(' pointagess ')
            print(pointagess)

            data = {
                "id":idsss,
                "prenom":prenommm,
                "nom":nommm,
                "telephone":telephonee,
                "email":emaill,
                "pointage": pointagess
            }
            tableau.append(data)





        #request.session['id'] = employerss.id
        return render(request, 'tables5.html', locals())




def edit_emp(request):
    if request.session.get('prenom') is None:
        print(' DANS DANS ')
        return render(request, 'login.html')
    else:

        test01 = request.GET["id"]

        print("test")
        print("test")
        print("test")
        print("test")
        print("test")
        print(test01)
        print(test01)
        print(test01)
        print(test01)

        us = request.session.get('id')
        employerss = employers.objects.get(id=test01)

        request.session['id'] = test01

        #request.session['id'] = employerss.id
        print(employerss)
        return render(request, 'forms2.html', locals())



def edit_emp_valid(request):
    if request.session.get('prenom') is None:
        print(' DANS DANS ')
        return render(request, 'login.html')
    else:

        # test = request.GET["id"]
        # us = request.session.get('id')
        test = request.session.get('id')

        print("test")
        print("test")
        print("test")
        print("test")
        print("test")

        print(test)
        print(test)
        print(test)
        print(test)
        print(test)

        #### us = request.session.get('id')

        employerss = employers.objects.get(id=test)


        ### request.POST["name_event"]
        if request.POST["ok"] == "Modifier":

            print("Modification ")
            print("Modification ")

            nom = request.POST["nom"]
            civilite = request.POST["civilite"]
            prenom = request.POST["prenom"]
            profession = request.POST["profession"]
            dateNaiss = request.POST["dateNaiss"]
            carte_didentite_nationale = request.POST["carte_didentite_nationale"]
            telephone = request.POST["telephone"]
            email = request.POST["email"]
            adresse = request.POST["adresse"]
            prenom1 = request.POST["prenom1"]
            nom1 = request.POST["nom1"]
            telephone1 = request.POST["telephone1"]
            prenom2 = request.POST["prenom2"]
            nom2 = request.POST["nom2"]
            telephone2 = request.POST["telephone2"]

            if employers.objects.filter(email=email).count() > 0:

                print(' employers.objects.filter(email=email).count() ')
                print(' employers.objects.filter(email=email).count() ')
                request.session['prenom'] = prenom
                request.session['nom'] = nom
                request.session['dateNaiss'] = dateNaiss
                request.session['adresse'] = adresse
                request.session['email'] = email
                request.session['profession'] = profession
                request.session['prenom1'] = prenom1
                request.session['nom1'] = nom1
                request.session['telephone1'] = telephone1
                request.session['prenom2'] = prenom2
                request.session['nom2'] = nom2
                request.session['telephone2'] = telephone2
                request.session['telephone'] = telephone
                request.session['carte_didentite_nationale'] = carte_didentite_nationale
                request.session['civilite'] = civilite
                # request.session['photo'] = image

                print(employers.objects.filter(email=email).count())
                message3 = "Le mail existe déjà en base. Veuillez le changer svp."
                return render(request, 'forms2.html', locals())

            elif employers.objects.filter(telephone=telephone).count() > 0:
                request.session['prenom'] = prenom
                request.session['nom'] = nom
                request.session['dateNaiss'] = dateNaiss
                request.session['adresse'] = adresse
                request.session['email'] = email
                request.session['profession'] = profession
                request.session['prenom1'] = prenom1
                request.session['nom1'] = nom1
                request.session['telephone1'] = telephone1
                request.session['prenom2'] = prenom2
                request.session['nom2'] = nom2
                request.session['telephone2'] = telephone2
                request.session['telephone'] = telephone
                request.session['carte_didentite_nationale'] = carte_didentite_nationale
                request.session['civilite'] = civilite
                # request.session['photo'] = image

                message2 = "Ce numéro de téléphone existe déjà en base. Veuillez le changer svp."
                return render(request, 'forms2.html', locals())

            elif employers.objects.filter(carte_didentite_nationale=carte_didentite_nationale).count() > 0:
                request.session['prenom'] = prenom
                request.session['nom'] = nom
                request.session['dateNaiss'] = dateNaiss
                request.session['adresse'] = adresse
                request.session['email'] = email
                request.session['profession'] = profession
                request.session['prenom1'] = prenom1
                request.session['nom1'] = nom1
                request.session['telephone1'] = telephone1
                request.session['prenom2'] = prenom2
                request.session['nom2'] = nom2
                request.session['telephone2'] = telephone2
                request.session['telephone'] = telephone
                request.session['carte_didentite_nationale'] = carte_didentite_nationale
                request.session['civilite'] = civilite
                # request.session['photo'] = image

                message1 = "Ce CIN existe déjà en base. Veuillez le changer svp."
                return render(request, 'forms2.html', locals())

            else:

                employerss.nom = request.POST["nom"]
                employerss.civilte = request.POST["civilite"]
                employerss.prenom = request.POST["prenom"]
                employerss.profession = request.POST["profession"]
                employerss.dateNaiss = request.POST["dateNaiss"]
                employerss.carte_didentite_nationale = request.POST["carte_didentite_nationale"]
                employerss.telephone = request.POST["telephone"]
                employerss.email = request.POST["email"]
                employerss.adresse = request.POST["adresse"]
                employerss.prenom1 = request.POST["prenom1"]
                employerss.nom1 = request.POST["nom1"]
                employerss.telephone1 = request.POST["telephone1"]
                employerss.prenom2 = request.POST["prenom2"]
                employerss.nom2 = request.POST["nom2"]
                employerss.telephone2 = request.POST["telephone2"]




                #employerss.photo2 = request.POST["photo"]
                print(' request.FILES["photo"] ')
                print(' request.FILES["photo"] ')

                #print(request.POST["photo"])
                if 'photo' in request.FILES:
                    employerss.photo2 = request.FILES["photo"]

                else:
                    print(' VIDE ')
                    print(' VIDE ')

                employerss.save()

                #request.session['id'] = employerss.id
                print(employerss)

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

                employess = employers.objects.all()
                nbEmployess = employers.objects.count()

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

                nbAbonnees1 = Paiement.objects.all().values('idPaiement', 'date_debut', 'date_fin', 'idUser',
                                                            'nbseances_en_cours', 'nbseances_total', 'dateencours',
                                                            'date_autorisation', 'datebadge')

                nbAbonnees2 = utilisateur2.objects.all().values('id', 'prenom', 'nom', 'civilite', 'dateNaiss', 'lieuNaiss',
                                                                'adresse', 'ville', 'email', 'profession', 'prenom1', 'nom1',
                                                                'telephone1', 'prenom2', 'nom2', 'telephone2', 'telephone',
                                                                'photo', 'id_typeabonnement')
                tableau = []

                comparer = str(datetime.now() - timedelta(days=30))
                print(" LA DATE DE COMPARAISON ")
                print(" LA DATE DE COMPARAISON ")
                print(" LA DATE DE COMPARAISON ")
                print(" LA DATE DE COMPARAISON ")
                print(" LA DATE DE COMPARAISON ")
                print(" LA DATE DE COMPARAISON ")
                print(comparer)
                print(comparer)
                print(comparer[:10])
                comparer0 = comparer[:10]

                # comparer0 = comparer[:10]

                formatter_string = "%Y-%m-%d"
                comparer1 = datetime.strptime(comparer0, formatter_string)

                print(" LLLLLLLLLLLLLLLLLLLLLLLLLL ")
                print(" LLLLLLLLLLLLLLLLLLLLLLLLLL ")
                print(" LLLLLLLLLLLLLLLLLLLLLLLLLL ")
                print(" LLLLLLLLLLLLLLLLLLLLLLLLLL ")
                print(" LLLLLLLLLLLLLLLLLLLLLLLLLL ")

                # for toto in nbAbonnees2:
                #     for toto1 in nbAbonnees1:
                #         print(" BAKHNA ")
                #         print(" BAKHNA ")
                #         print(" BAKHNA ")
                #         print(" BAKHNA ")
                #         print(toto1['datebadge'])
                #         print(toto1['datebadge'][:10])
                #         print(toto1['datebadge'])
                #         toto222 = datetime.strptime(toto1['datebadge'][:10], formatter_string)
                #         print(" toto222 ")
                #         print(" toto222 ")
                #         print(" toto222 ")
                #         print(" toto222 ")
                #         print(toto222)
                #         print(toto222)
                #         print(toto222)
                #
                #         # if toto['id'] == toto1['idUser'] and toto1['datebadge'] != "None" and toto1['datebadge'] <= comparer1:
                #         if toto['id'] == toto1['idUser'] and toto1['datebadge'] != "None" and toto1[
                #             'datebadge'] != "NULL" and datetime.strptime(str(toto1['datebadge']),
                #                                                          formatter_string) <= comparer1:
                #             data01 = {
                #                 "id": toto['id'],
                #                 "prenom": toto['prenom'],
                #                 "nom": toto['nom'],
                #                 "civilite": str(toto['civilite']),
                #                 "dateNaiss": str(toto['dateNaiss']),
                #                 "lieuNaiss": str(toto['lieuNaiss']),
                #                 "adresse": str(toto['adresse']),
                #                 "ville": str(toto['ville']),
                #                 "email": str(toto['email']),
                #                 "profession": str(toto['profession']),
                #                 "prenom1": str(toto['prenom1']),
                #                 "nom1": toto['nom1'],
                #                 "telephone1": toto['telephone1'],
                #                 "prenom2": str(toto['prenom2']),
                #                 "nom2": str(toto['nom2']),
                #                 "telephone2": str(toto['telephone2']),
                #                 "telephone": str(toto['telephone']),
                #                 "photo": str(toto['photo']),
                #                 "id_typeabonnement": toto['id_typeabonnement'],
                #                 "idPaiement": toto1['idPaiement'],
                #                 "date_debut": str(toto1['date_debut']),
                #                 "date_fin": str(toto1['date_fin']),
                #                 "nbseances_en_cours": toto1['nbseances_en_cours'],
                #                 "nbseances_total": toto1['nbseances_total'],
                #                 "dateencours": str(toto1['dateencours']),
                #                 "date_autorisation": str(toto1['date_autorisation']),
                #                 "datebadge": str(toto1['datebadge']),
                #             }
                #             tableau.append(data01)
                #             taille = len(tableau)

                return render(request, 'dashboard.html', locals())
            return render(request, 'dashboard.html', locals())

        else:

            if request.POST['ok'] == "Supprimer":
                print("Supprimer ")

                test = request.session.get('id')

                employerssss = employers.objects.get(id=test)
                employerssss.delete()

                nbAbonnees = utilisateur2.objects.count()
                nbEssai = personne_essaie.objects.count()

                employess = employers.objects.all()
                nbEmployess = employers.objects.count()

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

                nbAbonnees1 = Paiement.objects.all().values('idPaiement', 'date_debut', 'date_fin', 'idUser',
                                                            'nbseances_en_cours', 'nbseances_total', 'dateencours',
                                                            'date_autorisation', 'datebadge')

                nbAbonnees2 = utilisateur2.objects.all().values('id', 'prenom', 'nom', 'civilite', 'dateNaiss', 'lieuNaiss',
                                                                'adresse', 'ville', 'email', 'profession', 'prenom1',
                                                                'nom1',
                                                                'telephone1', 'prenom2', 'nom2', 'telephone2', 'telephone',
                                                                'photo', 'id_typeabonnement')
                tableau = []

                comparer = str(datetime.now() - timedelta(days=30))
                print(" LA DATE DE COMPARAISON ")
                print(" LA DATE DE COMPARAISON ")
                print(" LA DATE DE COMPARAISON ")
                print(" LA DATE DE COMPARAISON ")
                print(" LA DATE DE COMPARAISON ")
                print(" LA DATE DE COMPARAISON ")
                print(comparer)
                print(comparer)
                print(comparer[:10])
                comparer0 = comparer[:10]

                # comparer0 = comparer[:10]

                formatter_string = "%Y-%m-%d"
                comparer1 = datetime.strptime(comparer0, formatter_string)

                print(" LLLLLLLLLLLLLLLLLLLLLLLLLL ")
                print(" LLLLLLLLLLLLLLLLLLLLLLLLLL ")
                print(" LLLLLLLLLLLLLLLLLLLLLLLLLL ")
                print(" LLLLLLLLLLLLLLLLLLLLLLLLLL ")
                print(" LLLLLLLLLLLLLLLLLLLLLLLLLL ")

                # for toto in nbAbonnees2:
                #     for toto1 in nbAbonnees1:
                #         print(" BAKHNA ")
                #         print(" BAKHNA ")
                #         print(" BAKHNA ")
                #         print(" BAKHNA ")
                #         print(toto1['datebadge'])
                #         print(toto1['datebadge'][:10])
                #         print(toto1['datebadge'])
                #         toto222 = datetime.strptime(toto1['datebadge'][:10], formatter_string)
                #         print(" toto222 ")
                #         print(" toto222 ")
                #         print(" toto222 ")
                #         print(" toto222 ")
                #         print(toto222)
                #         print(toto222)
                #         print(toto222)
                #
                #         # if toto['id'] == toto1['idUser'] and toto1['datebadge'] != "None" and toto1['datebadge'] <= comparer1:
                #         if toto['id'] == toto1['idUser'] and toto1['datebadge'] != "None" and toto1[
                #             'datebadge'] != "NULL" and datetime.strptime(str(toto1['datebadge']),
                #                                                          formatter_string) <= comparer1:
                #             data01 = {
                #                 "id": toto['id'],
                #                 "prenom": toto['prenom'],
                #                 "nom": toto['nom'],
                #                 "civilite": str(toto['civilite']),
                #                 "dateNaiss": str(toto['dateNaiss']),
                #                 "lieuNaiss": str(toto['lieuNaiss']),
                #                 "adresse": str(toto['adresse']),
                #                 "ville": str(toto['ville']),
                #                 "email": str(toto['email']),
                #                 "profession": str(toto['profession']),
                #                 "prenom1": str(toto['prenom1']),
                #                 "nom1": toto['nom1'],
                #                 "telephone1": toto['telephone1'],
                #                 "prenom2": str(toto['prenom2']),
                #                 "nom2": str(toto['nom2']),
                #                 "telephone2": str(toto['telephone2']),
                #                 "telephone": str(toto['telephone']),
                #                 "photo": str(toto['photo']),
                #                 "id_typeabonnement": toto['id_typeabonnement'],
                #                 "idPaiement": toto1['idPaiement'],
                #                 "date_debut": str(toto1['date_debut']),
                #                 "date_fin": str(toto1['date_fin']),
                #                 "nbseances_en_cours": toto1['nbseances_en_cours'],
                #                 "nbseances_total": toto1['nbseances_total'],
                #                 "dateencours": str(toto1['dateencours']),
                #                 "date_autorisation": str(toto1['date_autorisation']),
                #                 "datebadge": str(toto1['datebadge']),
                #             }
                #             tableau.append(data01)
                #             taille = len(tableau)

                return render(request, 'dashboard.html', locals())

                #return render(request, 'forms.html', locals())
                #return render(request, 'dashboard.html', locals())
            else:
                print("Autres  ")

                nbAbonnees = utilisateur2.objects.count()
                nbEssai = personne_essaie.objects.count()

                datedebut = datetime.now()

                employess = employers.objects.all()
                nbEmployess = employers.objects.count()

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

                nbAbonnees1 = Paiement.objects.all().values('idPaiement', 'date_debut', 'date_fin', 'idUser',
                                                            'nbseances_en_cours', 'nbseances_total', 'dateencours',
                                                            'date_autorisation', 'datebadge')

                nbAbonnees2 = utilisateur2.objects.all().values('id', 'prenom', 'nom', 'civilite', 'dateNaiss', 'lieuNaiss',
                                                                'adresse', 'ville', 'email', 'profession', 'prenom1',
                                                                'nom1',
                                                                'telephone1', 'prenom2', 'nom2', 'telephone2', 'telephone',
                                                                'photo', 'id_typeabonnement')
                tableau = []

                comparer = str(datetime.now() - timedelta(days=30))
                print(" LA DATE DE COMPARAISON ")
                print(" LA DATE DE COMPARAISON ")
                print(" LA DATE DE COMPARAISON ")
                print(" LA DATE DE COMPARAISON ")
                print(" LA DATE DE COMPARAISON ")
                print(" LA DATE DE COMPARAISON ")
                print(comparer)
                print(comparer)
                print(comparer[:10])
                comparer0 = comparer[:10]

                # comparer0 = comparer[:10]

                formatter_string = "%Y-%m-%d"
                comparer1 = datetime.strptime(comparer0, formatter_string)

                print(" LLLLLLLLLLLLLLLLLLLLLLLLLL ")
                print(" LLLLLLLLLLLLLLLLLLLLLLLLLL ")
                print(" LLLLLLLLLLLLLLLLLLLLLLLLLL ")
                print(" LLLLLLLLLLLLLLLLLLLLLLLLLL ")
                print(" LLLLLLLLLLLLLLLLLLLLLLLLLL ")

                # for toto in nbAbonnees2:
                #     for toto1 in nbAbonnees1:
                #         print(" BAKHNA ")
                #         print(" BAKHNA ")
                #         print(" BAKHNA ")
                #         print(" BAKHNA ")
                #         print(toto1['datebadge'])
                #         print(toto1['datebadge'][:10])
                #         print(toto1['datebadge'])
                #         toto222 = datetime.strptime(toto1['datebadge'][:10], formatter_string)
                #         print(" toto222 ")
                #         print(" toto222 ")
                #         print(" toto222 ")
                #         print(" toto222 ")
                #         print(toto222)
                #         print(toto222)
                #         print(toto222)
                #
                #         # if toto['id'] == toto1['idUser'] and toto1['datebadge'] != "None" and toto1['datebadge'] <= comparer1:
                #         if toto['id'] == toto1['idUser'] and toto1['datebadge'] != "None" and toto1[
                #             'datebadge'] != "NULL" and datetime.strptime(str(toto1['datebadge']),
                #                                                          formatter_string) <= comparer1:
                #             data01 = {
                #                 "id": toto['id'],
                #                 "prenom": toto['prenom'],
                #                 "nom": toto['nom'],
                #                 "civilite": str(toto['civilite']),
                #                 "dateNaiss": str(toto['dateNaiss']),
                #                 "lieuNaiss": str(toto['lieuNaiss']),
                #                 "adresse": str(toto['adresse']),
                #                 "ville": str(toto['ville']),
                #                 "email": str(toto['email']),
                #                 "profession": str(toto['profession']),
                #                 "prenom1": str(toto['prenom1']),
                #                 "nom1": toto['nom1'],
                #                 "telephone1": toto['telephone1'],
                #                 "prenom2": str(toto['prenom2']),
                #                 "nom2": str(toto['nom2']),
                #                 "telephone2": str(toto['telephone2']),
                #                 "telephone": str(toto['telephone']),
                #                 "photo": str(toto['photo']),
                #                 "id_typeabonnement": toto['id_typeabonnement'],
                #                 "idPaiement": toto1['idPaiement'],
                #                 "date_debut": str(toto1['date_debut']),
                #                 "date_fin": str(toto1['date_fin']),
                #                 "nbseances_en_cours": toto1['nbseances_en_cours'],
                #                 "nbseances_total": toto1['nbseances_total'],
                #                 "dateencours": str(toto1['dateencours']),
                #                 "date_autorisation": str(toto1['date_autorisation']),
                #                 "datebadge": str(toto1['datebadge']),
                #             }
                #             tableau.append(data01)
                #             taille = len(tableau)

                return render(request, 'dashboard.html', locals())

                #return render(request, 'forms.html', locals())
                #return render(request, 'dashboard.html', locals())




def calculdutempsold(request):

    #### pointages = pointage.objects.all()

    pointages01 = pointage.objects.filter(idUser=1).values('id', 'idUser', 'date_et_heures')
    listeDate = []
    listeHeures = []
    listeCalculTotal = []

    fmt = '%H:%M'
    resultatlast = datetime.strptime("00:00", fmt)
    resultatlast2 = datetime.strptime("00:00", fmt)

    resultat = datetime.strptime("00:00", fmt)

    hh11 = 0
    mm11 = 0
    hh22 = 0
    mm22 = 0

    resultatlast10 = ""
    resultatlast11 = ""
    resultatfinal = ""
    resultatfinalh1 = ""
    resultatfinalm1 = ""
    resultatfinalsshh1=0
    resultatfinalssmm1=0

    valeurPaire = datetime.strptime("00:00", fmt)
    valeurImpaire = datetime.strptime("00:00", fmt)

    print("pointages01")
    print(pointages01)

    if len(pointages01) != 0:

        for pointa in pointages01:

            if pointa['date_et_heures'][:10] in listeDate:

                fmt = '%H:%M'
                if pointa['date_et_heures'][15:16] != ":":

                    h1 = datetime.strptime(pointa['date_et_heures'][11:16], fmt)
                    h2 = datetime.strptime(listeHeures[-1], fmt)
                    resultat = h1-h2
                    listeCalculTotal.append(resultat)

                else:

                    h1 = datetime.strptime(pointa['date_et_heures'][11:15], fmt)
                    h2 = datetime.strptime(listeHeures[-1], fmt)
                    resultat = h1 - h2
                    listeCalculTotal.append(resultat)



            else:

                listeCalculTotal = []

                if pointa['date_et_heures'][15:16] != ":":
                    listeDate.append(pointa['date_et_heures'][:10])
                    listeHeures.append(pointa['date_et_heures'][11:16])

                else:

                    listeDate.append(pointa['date_et_heures'][:10])
                    listeHeures.append(pointa['date_et_heures'][11:15])


            print(" La valeur de la liste déroulante ")
            print(listeDate)
            print(listeDate)

            print(" La valeur de la liste déroulante ")
            print(listeHeures)
            print(listeHeures)


        return render(request, 'forms.html')

    print(" PAS DE POINTAGE HORAIRES ")
    print(" PAS DE POINTAGE HORAIRES ")
    return render(request, 'forms.html')









def calculdutemps(request):
    if request.session.get('prenom') is None:
        print(' DANS DANS ')
        return render(request, 'login.html')
    else:
        tableauTout = []
        tableauTout1 = []
        tableauTout2 = []

        us = request.session.get('id')
        test01 = request.GET["id"]

        ids = request.session.get('id')
        print(" us001 ")
        print(" us001 ")
        print(" us001 ")
        print(" us001 ")
        print(" us001 ")
        print(" us001 ")
        print(" us001 ")
        print(us)
        print(us)
        print(us)

        employess = employers.objects.all()
        nbEmployess = employers.objects.count()

        personne = employers.objects.get(id=test01)
        personneNom =personne.nom
        personnePreNom =personne.prenom
        personneEmail =personne.email
        personneTelephone =personne.telephone

        nbPassages = pointage.objects.filter(idUser=test01).count()



        pointages01 = pointage.objects.filter(idUser=test01).values('id', 'idUser', 'date_et_heures')
        listeDate = []
        listeHeures = []
        listeCalculTotal = []
        finalValidator = []

        fmt = '%H:%M'
        resultatlast = datetime.strptime("00:00", fmt)
        resultatlast2 = datetime.strptime("00:00", fmt)

        resultat = datetime.strptime("00:00", fmt)

        hh11 = 0
        mm11 = 0
        hh22 = 0
        mm22 = 0

        resultatlast10 = ""
        resultatlast11 = ""
        resultatfinal = ""
        resultatfinalh1 = ""
        resultatfinalm1 = ""
        resultatfinalsshh1=0
        resultatfinalssmm1=0

        valeurPaire = datetime.strptime("00:00", fmt)
        valeurImpaire = datetime.strptime("00:00", fmt)

        if len(pointages01) != 0:

            for pointa in pointages01:

                if pointa['date_et_heures'][:10] in listeDate:

                    fmt = '%H:%M'
                    if pointa['date_et_heures'][15:16] != ":":

                        h1 = datetime.strptime(pointa['date_et_heures'][11:16], fmt)
                        h2 = datetime.strptime(listeHeures[-1], fmt)
                        resultat = h1-h2
                        listeCalculTotal.append(resultat)

                        print(' listeCalculTotal 1')
                        print(' listeCalculTotal 1')
                        print(' listeCalculTotal 1')
                        print(listeCalculTotal)
                        print(listeCalculTotal)
                        print(listeCalculTotal)

                    else:

                        h1 = datetime.strptime(pointa['date_et_heures'][11:15], fmt)
                        h2 = datetime.strptime(listeHeures[-1], fmt)
                        resultat = h1 - h2
                        listeCalculTotal.append(resultat)

                        print(' listeCalculTotal 2')
                        print(' listeCalculTotal 2')
                        print(' listeCalculTotal 2')
                        print(listeCalculTotal)
                        print(listeCalculTotal)
                        print(listeCalculTotal)



                    if len(listeCalculTotal) != 0:

                        for listCal in range(len(listeCalculTotal)):

                            lavaleurnormale = str(listeCalculTotal[listCal])

                            if (listCal+1)%2==0:

                                if len(lavaleurnormale)==7:

                                    lavaleurnormale = lavaleurnormale[:4]
                                    hh11 = lavaleurnormale[:1]
                                    mm11 = lavaleurnormale[2:4]


                                else:

                                    lavaleurnormale = lavaleurnormale[:5]
                                    hh11 = lavaleurnormale[:1]
                                    mm11 = lavaleurnormale[3:5]


                                if len(listeCalculTotal)-1 == listCal:
                                    print(' LA VALEUR DU TABLEAU 1')
                                    print(' LA VALEUR DU TABLEAU 1')
                                    print(' LA VALEUR DU TABLEAU 1')
                                    print(' LA VALEUR DU TABLEAU 1')
                                    print(listeCalculTotal)
                                    print(listeHeures[-1])

                                    valeurPaire = valeurPaire+timedelta(hours=int(hh11), minutes=int(mm11))
                                    print(valeurPaire)
                                    print('VALEUR PAIRE ')
                                    print('VALEUR PAIRE ')
                                    print('VALEUR PAIRE ')
                                    print(valeurPaire)




                            else:

                                lavaleurnormale = str(listeCalculTotal[listCal])

                                if len(lavaleurnormale)==7:

                                    lavaleurnormale = lavaleurnormale[:4]
                                    hh22 = lavaleurnormale[:1]
                                    mm22 = lavaleurnormale[2:4]

                                else:

                                    lavaleurnormale = lavaleurnormale[:5]
                                    hh22 = lavaleurnormale[:2]
                                    mm22 = lavaleurnormale[3:5]


                                if len(listeCalculTotal)-1 == listCal:

                                    print(' LA VALEUR DU TABLEAU 2')
                                    print(' LA VALEUR DU TABLEAU 2')
                                    print(' LA VALEUR DU TABLEAU 2')
                                    print(' LA VALEUR DU TABLEAU 2')
                                    print(listeCalculTotal)
                                    print(listeHeures[-1])



                                    valeurImpaire = valeurImpaire+timedelta(hours=int(hh22), minutes=int(mm22))
                                    print(valeurImpaire)






                            if len(finalValidator) != 0:


                                for liste in finalValidator:

                                    for k, v in liste.items():

                                        if pointa['date_et_heures'][:10] == v:
                                            print(" BAKHNA ")
                                            print(" BAKHNA ")
                                            print(valeurPaire)
                                            print(valeurImpaire)

                                            finalValidator[-1]["date"] = pointa['date_et_heures'][:10]
                                            finalValidator[-1]["travail"] = valeurImpaire
                                            finalValidator[-1]["repos"] = valeurPaire



                            else:
                                data = {
                                    "date": pointa['date_et_heures'][:10],
                                    "travail": valeurImpaire,
                                    "repos": valeurPaire,
                                }
                                finalValidator.append(data)
                                print(' finalValidator ')
                                print(' finalValidator ')
                                print(' finalValidator ')
                                print(finalValidator)
                                print(" listeHeures[-1] ")
                                print(" listeHeures[-1] ")
                                print(" listeHeures[-1] ")
                                print(" listeHeures[-1] ")
                                print(listeHeures[-1])

                    ## Contrôle de saisit pour eliminer les 2 codes
                    if pointa['date_et_heures'][15:16] != ":":
                        listeHeures.append(pointa['date_et_heures'][11:16])
                    else:
                        listeHeures.append(pointa['date_et_heures'][11:15])


                    #print(" finalValidator ")
                    #print(finalValidator)

                else:

                    #listeCalculTotal = []
                    print(" ELSE GÉNÉRAL ")
                    print(" ELSE GÉNÉRAL ")
                    print(" ELSE GÉNÉRAL ")
                    print(" ELSE GÉNÉRAL ")

                    listeHeures[:]=[]
                    data1 = {
                        "date": pointa['date_et_heures'][:10],
                        "travail": 0,
                        "repos": 0
                    }
                    finalValidator.append(data1)
                    valeurPaire = datetime.strptime("00:00", fmt)
                    valeurImpaire = datetime.strptime("00:00", fmt)


                    print(data1)
                    print(finalValidator)

                    if pointa['date_et_heures'][15:16] != ":":
                        listeDate.append(pointa['date_et_heures'][:10])
                        listeHeures.append(pointa['date_et_heures'][11:16])
                        listeCalculTotal[:]=[]
                        print(" listeHeures ")
                        print(" listeHeures ")
                        print(listeHeures)

                    else:

                        listeDate.append(pointa['date_et_heures'][:10])
                        listeHeures.append(pointa['date_et_heures'][11:15])
                        listeCalculTotal[:]=[]


                print(" La valeur de la liste déroulante ")
                print(listeDate)
                print(listeDate)

                print(" La valeur de la liste déroulante ")
                print(listeHeures)
                print(listeHeures)



            print(resultat)
            print(listeCalculTotal)

            ## Contrôle de saisit pour eliminer les 2 codes
            if pointa['date_et_heures'][15:16] != ":":
                listeHeures.append(pointa['date_et_heures'][11:16])
            else:
                listeHeures.append(pointa['date_et_heures'][11:15])


            print(" LA DERNIERE VALEUR ")
            print(" LA DERNIERE VALEUR ")
            print(" LA DERNIERE VALEUR ")
            print(" LA DERNIERE VALEUR ")
            print(" LA DERNIERE VALEUR ")



            print(finalValidator)
            return render(request, 'forms3.html', locals())

        print(" PAS DE POINTAGE HORAIRES ")
        print(" PAS DE POINTAGE HORAIRES ")
        return render(request, 'forms3.html', locals())




#775535309


def calculdutemps_bon_avant_changement(request):
    if request.session.get('prenom') is None:
        print(' DANS DANS ')
        return render(request, 'login.html')
    else:

        us = request.session.get('id')
        test01 = request.GET["id"]

        ids = request.session.get('id')
        print(" us001 ")
        print(" us001 ")
        print(" us001 ")
        print(" us001 ")
        print(" us001 ")
        print(" us001 ")
        print(" us001 ")
        print(us)
        print(us)
        print(us)

        employess = employers.objects.all()
        nbEmployess = employers.objects.count()

        personne = employers.objects.get(id=test01)
        personneNom =personne.nom
        personnePreNom =personne.prenom
        personneEmail =personne.email
        personneTelephone =personne.telephone

        nbPassages = pointage.objects.filter(idUser=test01).count()



        pointages01 = pointage.objects.filter(idUser=test01).values('id', 'idUser', 'date_et_heures')
        listeDate = []
        listeHeures = []
        listeCalculTotal = []
        finalValidator = []

        fmt = '%H:%M'
        resultatlast = datetime.strptime("00:00", fmt)
        resultatlast2 = datetime.strptime("00:00", fmt)

        resultat = datetime.strptime("00:00", fmt)

        hh11 = 0
        mm11 = 0
        hh22 = 0
        mm22 = 0

        resultatlast10 = ""
        resultatlast11 = ""
        resultatfinal = ""
        resultatfinalh1 = ""
        resultatfinalm1 = ""
        resultatfinalsshh1=0
        resultatfinalssmm1=0

        valeurPaire = datetime.strptime("00:00", fmt)
        valeurImpaire = datetime.strptime("00:00", fmt)

        if len(pointages01) != 0:



            for pointa in pointages01:



                if pointa['date_et_heures'][:10] in listeDate:

                    fmt = '%H:%M'
                    if pointa['date_et_heures'][15:16] != ":":

                        h1 = datetime.strptime(pointa['date_et_heures'][11:16], fmt)
                        h2 = datetime.strptime(listeHeures[-1], fmt)
                        resultat = h1-h2
                        listeCalculTotal.append(resultat)

                    else:

                        h1 = datetime.strptime(pointa['date_et_heures'][11:15], fmt)
                        h2 = datetime.strptime(listeHeures[-1], fmt)
                        resultat = h1 - h2
                        listeCalculTotal.append(resultat)

                    if len(listeCalculTotal) != 0:


                        for listCal in range(len(listeCalculTotal)):

                            lavaleurnormale = str(listeCalculTotal[listCal])

                            if (listCal+1)%2==0:

                                if len(lavaleurnormale)==7:

                                    lavaleurnormale = lavaleurnormale[:4]
                                    hh11 = lavaleurnormale[:1]
                                    mm11 = lavaleurnormale[2:4]

                                else:

                                    lavaleurnormale = lavaleurnormale[:5]
                                    hh11 = lavaleurnormale[:1]
                                    mm11 = lavaleurnormale[3:5]

                                if len(listeCalculTotal)-1 == listCal:
                                    valeurPaire = valeurPaire+timedelta(hours=int(hh11), minutes=int(mm11))
                                    print(valeurPaire)

                            else:

                                lavaleurnormale = str(listeCalculTotal[listCal])

                                if len(lavaleurnormale)==7:

                                    lavaleurnormale = lavaleurnormale[:4]
                                    hh22 = lavaleurnormale[:1]
                                    mm22 = lavaleurnormale[2:4]

                                else:

                                    lavaleurnormale = lavaleurnormale[:5]
                                    hh22 = lavaleurnormale[:2]
                                    mm22 = lavaleurnormale[3:5]


                                if len(listeCalculTotal)-1 == listCal:
                                    valeurImpaire = valeurImpaire+timedelta(hours=int(hh22), minutes=int(mm22))
                                    print(valeurImpaire)




                            if len(finalValidator) != 0:


                                for liste in finalValidator:

                                    for k, v in liste.items():

                                        if pointa['date_et_heures'][:10] == v:
                                            print(" BAKHNA ")
                                            print(" BAKHNA ")
                                            print(valeurPaire)
                                            print(valeurImpaire)

                                            finalValidator[-1]["date"] = pointa['date_et_heures'][:10]
                                            finalValidator[-1]["travail"] = valeurImpaire
                                            finalValidator[-1]["repos"] = valeurPaire

                            else:
                                data = {
                                    "date": pointa['date_et_heures'][:10],
                                    "travail": valeurImpaire,
                                    "repos": valeurPaire
                                }
                                finalValidator.append(data)


                    ## Contrôle de saisit pour eliminer les 2 codes
                    if pointa['date_et_heures'][15:16] != ":":
                        listeHeures.append(pointa['date_et_heures'][11:16])
                    else:
                        listeHeures.append(pointa['date_et_heures'][11:15])


                    #print(" finalValidator ")
                    #print(finalValidator)

                else:

                    #listeCalculTotal = []
                    print(" ELSE GÉNÉRAL ")
                    print(" ELSE GÉNÉRAL ")
                    print(" ELSE GÉNÉRAL ")
                    print(" ELSE GÉNÉRAL ")

                    listeHeures[:]=[]
                    data1 = {
                        "date": pointa['date_et_heures'][:10],
                        "travail": 0,
                        "repos": 0
                    }
                    finalValidator.append(data1)
                    valeurPaire = datetime.strptime("00:00", fmt)
                    valeurImpaire = datetime.strptime("00:00", fmt)


                    print(data1)
                    print(finalValidator)

                    if pointa['date_et_heures'][15:16] != ":":
                        listeDate.append(pointa['date_et_heures'][:10])
                        listeHeures.append(pointa['date_et_heures'][11:16])
                        listeCalculTotal[:]=[]
                        print(" listeHeures ")
                        print(" listeHeures ")
                        print(listeHeures)

                    else:

                        listeDate.append(pointa['date_et_heures'][:10])
                        listeHeures.append(pointa['date_et_heures'][11:15])
                        listeCalculTotal[:]=[]




                print(" La valeur de la liste déroulante ")
                print(listeDate)
                print(listeDate)

                print(" La valeur de la liste déroulante ")
                print(listeHeures)
                print(listeHeures)



            # if len(listeCalculTotal) != 0:
            #
            #     print("###### DIOP FALL MBEUK ##### ")
            #     print("###### DIOP FALL MBEUK ##### ")
            #     print("###### DIOP FALL MBEUK ##### ")
            #     print("###### DIOP FALL MBEUK ##### ")
            #     print("###### DIOP FALL MBEUK ##### ")
            #     print("###### DIOP FALL MBEUK ##### ")
            #
            #     for listCal in range(len(listeCalculTotal)):
            #
            #         print(" LA VALEUR DU BOUCLE ==>> " + str(listCal))
            #         print(" LA VALEUR DU BOUCLE ==>> " + str(listCal))
            #         print(" LA VALEUR DU range ==>> " + str(len(listeCalculTotal)))
            #         print(" LA VALEUR DU len ==>> " + str(len(listeCalculTotal)))
            #         print(" LA VALEUR DU BOUCLE ==>> " + str(listeCalculTotal[listCal]))
            #         print(" FINAL " + str(listeCalculTotal))
            #
            #         lavaleurnormale = str(listeCalculTotal[listCal])
            #
            #         if (listCal + 1) % 2 == 0:
            #
            #             if len(lavaleurnormale) == 7:
            #
            #                 lavaleurnormale = lavaleurnormale[:4]
            #                 hh11 = lavaleurnormale[:1]
            #                 mm11 = lavaleurnormale[2:4]
            #
            #             else:
            #
            #                 lavaleurnormale = lavaleurnormale[:5]
            #                 hh11 = lavaleurnormale[:1]
            #                 mm11 = lavaleurnormale[3:5]
            #
            #             if len(listeCalculTotal) - 1 == listCal:
            #                 valeurPaire = valeurPaire + timedelta(hours=int(hh11), minutes=int(mm11))
            #
            #         else:
            #
            #             lavaleurnormale = str(listeCalculTotal[listCal])
            #             if len(lavaleurnormale) == 7:
            #
            #                 lavaleurnormale = lavaleurnormale[:4]
            #                 hh22 = lavaleurnormale[:1]
            #                 mm22 = lavaleurnormale[2:4]
            #
            #             else:
            #                 lavaleurnormale = lavaleurnormale[:5]
            #                 hh22 = lavaleurnormale[:2]
            #                 mm22 = lavaleurnormale[3:5]
            #
            #             if len(listeCalculTotal) - 1 == listCal:
            #                 valeurImpaire = valeurImpaire + timedelta(hours=int(hh22), minutes=int(mm22))
            #
            #             print(valeurImpaire)
            #             print(valeurPaire)
            #             data = {
            #                 "date": pointa['date_et_heures'][:10],
            #                 "travail": valeurImpaire,
            #                 "repos": valeurPaire
            #             }
            #
            #             finalValidator.append(data)
            #             print(" THE END ")
            #             print(" THE END ")
            #             print(" THE END ")
            #             print(" THE END ")
            #             # print(data)
            #             print(finalValidator)
            #


            print(resultat)
            print(listeCalculTotal)

            ## Contrôle de saisit pour eliminer les 2 codes
            if pointa['date_et_heures'][15:16] != ":":
                listeHeures.append(pointa['date_et_heures'][11:16])
            else:
                listeHeures.append(pointa['date_et_heures'][11:15])


            print(" LA DERNIERE VALEUR ")
            print(" LA DERNIERE VALEUR ")
            print(" LA DERNIERE VALEUR ")
            print(" LA DERNIERE VALEUR ")
            print(" LA DERNIERE VALEUR ")

            print(finalValidator)
            return render(request, 'forms3.html', locals())

        print(" PAS DE POINTAGE HORAIRES ")
        print(" PAS DE POINTAGE HORAIRES ")
        return render(request, 'forms3.html', locals())

