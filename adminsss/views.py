from django.shortcuts import render
from adminsss.models import *
from essaies.models import *
from adminsss.models import *
from users.models import *
from datetime import datetime, timedelta
from rest_framework.response import Response
from datetime import datetime, timedelta
from django.db.models import Max
from django.db.models import Count, Sum, Avg, Min
import itertools
from django.core.mail import send_mail, BadHeaderError
from random import randint
from django.db.models import Q
from datetime import datetime
from itertools import *
from employers.models import *
from datetime import datetime, timedelta
import calendar




def forgetpassword(request):
    return render(request, 'forgetaccount.html', locals())


def inscription(request):
    return render(request, 'inscription.html', locals())



def send_email_password(request):


    try:
        user = adminss.objects.get(email=request.POST['email'])

        print (user)
        new_password = randint(1000, 1000000)
        user.password= new_password
        user.save()
        send_mail(' Nouveau Mot de passe',
                  'Voici votre nouveau mot de passe  ' + str(new_password),
                  'elitefitnessclubkebe@gmail.com', [request.POST['email']])
        message = ' Votre mot de passe a été envoyé par mail '
        return render(request, 'login.html', {'message': message})

    except:

        message = ' Votre mail ne se trouve pas sur la base de données'
        return render(request, 'forgetaccount.html', {'message': message})






def inscription1(request):

    prenom = request.POST['prenom']
    nom = request.POST['nom']
    email = request.POST['email']
    telephone = request.POST['telephone']
    password1 = request.POST['password1']
    password2 = request.POST['password2']


    try:
        us = adminss.objects.filter(Q(email=email) & Q(is_active=False))

        us1 = adminss.objects.filter(telephone=telephone, email=email, is_active=False).values('prenom',
                                                                                               'nom',
                                                                                               'telephone',
                                                                                               'email',
                                                                                               'password',
                                                                                               'id',
                                                                                               'activation_token')


        if len(us) > 0:

            if password1 == password2:

                try:
                    code = randint(100000, 1000000)
                    # us.update(password=new_password)

                    # user = User()
                    print(' DANS PASSWORD ')

                    us.update(email=email)
                    us.update(prenom=prenom)
                    us.update(nom=nom)
                    us.update(telephone=telephone)
                    us.update(password=password1)


                    send_mail('Code de Validation', 'Le code de Validation est : ' + str(us1[0]['activation_token']),
                              'elitefitnessclubkebe@gmail.com', [email])

                    return render(request, 'inscription1.html', {'user': us1[0]['id']})


                except:

                    print(' COOL ')

                    request.session['first_name'] = us1[0]['first_name']
                    request.session['last_name'] = us1[0]['last_name']
                    request.session['email'] = us1[0]['email']
                    request.session['telephone'] = us1[0]['telephone']

                    message_password = 'E-mail ou téléphone existant.'
                    print(' E-mail ou téléphone existant. ')
                    return render(request, 'inscription.html', locals())




            else:
                print(' COOL ')

                request.session['first_name'] = us1[0]['first_name']
                request.session['last_name'] = us1[0]['last_name']
                request.session['email'] = us1[0]['email']
                request.session['telephone'] = us1[0]['telephone']

                message_password = 'Les mots de passe ne sont pas identiques.'
                print(' Password non identique ')
                return render(request, 'inscription.html',
                              locals())


        else:
            # return render(request, 'office/register2.html', {'user': us.id})

            print(' ELSE ')
            if password1 == password2:
                print(' cool ')
                try:

                    code = randint(100000, 1000000)
                    user = adminss()

                    user.prenom = prenom
                    user.nom = nom
                    user.telephone = telephone
                    user.email = email
                    user.password = password1
                    user.activation_token = code
                    user.is_active = False
                    user.save()

                    print('cool sms ')
                    print(' avant mail ')

                    send_mail('Code de Validation', 'Le code de Validation est : ' + str(user.activation_token),
                              'elitefitnessclubkebe@gmail.com', [str(email)])

                    print(' Mail Non envoyé ')
                    return render(request, 'inscription1.html', {'user': user.id})

                except:

                    adminss.objects.get(email=email)
                    message_email = 'E-mail existant ou téléphone existant.'
                    print('Email  Existant')
                    return render(request, 'inscription.html', locals())



            else:

                print(' COOL ')
                request.session['prenom'] = prenom
                request.session['nom'] = nom
                request.session['email'] = email
                request.session['telephone'] = telephone

                message_password = 'Les mots de passe ne sont pas identiques.'
                print(' Password non identique ')
                return render(request, 'inscription.html',
                              locals())




    except:

        usssssss = adminss.objects.filter(email=email, telephone=telephone, is_active=True)
        if len(usssssss)>0:

            # message_email = 'E-mail existant.'
            message_email = 'Votre compte est activé. Veuillez vous connecter.'
            print('Email  Existant')
            return render(request, 'inscription.html', locals())

        message_password = 'L\'email n\'est pas associé à votre téléphone.'
        return render(request, 'inscription.html',
                      locals())




def inscription2(request):

    # u = User.objects.get(activation_token=request.POST.get('user.activation_token'))
    try:
        u = adminss.objects.get(activation_token=request.POST['code'])
        u.is_active = True
        u.save()
        message_code = 'Bienvenue sur EFC : votre compte est activé avec succès.'
        send_mail(' Inscription fait avec success',
                  u.prenom+'  '+ u.nom + ' Bienvenue sur EFC : votre compte est activé avec succès.',
                  'elitefitnessclubkebe@gmail.com', [u.email])
        return render(request, 'login.html', {'message_code': message_code})

    except:
        message_code = 'Vérifiez le code d’activation reçu par Mail.'
        print (' Code d activation non identique ')
        return render(request, 'inscription1.html',
                      {'message_password': message_code})





def table007(request):
    if request.session.get('prenom') is None:
        print(' DANS DANS ')
        return render(request, 'login.html')

    else:

        employess = employers.objects.all()
        nbEmployess = employers.objects.count()

        abonnes = utilisateur2.objects.all()

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
        return render(request, 'tables8.html', locals())


def statTrancheDate(request):
    if request.session.get('prenom') is None:
        print(' DANS DANS ')
        return render(request, 'login.html')
    else:

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
        if request.method == "POST":
            start_date = request.POST['date_de_debut']
            end_date = request.POST['date_de_fin']
            stat = Statisque.objects.filter(date_heure__range=(start_date, end_date)).values('id', 'date_heure', 'idUser', 'idUser__nom', 'idUser__prenom', 'idUser__civilite', 'idUser__dateNaiss')
            print(stat)
            return render(request, 'tables8.html', locals())



def statistique(request):

    if request.session.get('prenom') is None:
        print(' DANS DANS ')
        return render(request, 'login.html')
    else:
        employess = employers.objects.all()
        nbEmployess = employers.objects.count()
        statistiques = Statisque.objects.all()
        return render(request, 'statisque.html', {'statistiques':statistiques})


def table7(request):
    if request.session.get('prenom') is None:
        print(' DANS DANS ')
        return render(request, 'login.html')
    else:
        employess = employers.objects.all()
        nbEmployess = employers.objects.count()
        abonnes = utilisateur2.objects.all()
        return render(request, 'tables7.html', locals())

def statDetailAbonne(request):
    if request.session.get('prenom') is None:
        print(' DANS DANS ')
        return render(request, 'login.html')
    else:

        employess = employers.objects.all()
        nbEmployess = employers.objects.count()

        nombreAnne = 0
        test01 = request.GET["id"]
        stat = Statisque.objects.filter(idUser=test01).values('id', 'date_heure', 'idUser', 'idUser__nom', 'idUser__prenom', 'idUser__civilite', 'idUser__dateNaiss', 'idUser__telephone')

        print(' stat ')
        print(' stat ')
        print(' stat ')
        print(stat)
        print(stat)
        print(stat)
        print(stat)

        print('Statisque.objects.filter(idUser=test01).count() ')
        print('Statisque.objects.filter(idUser=test01).count() ')
        print('Statisque.objects.filter(idUser=test01).count() ')
        print(Statisque.objects.filter(idUser=test01).count())
        print(Statisque.objects.filter(idUser=test01).count())
        print(Statisque.objects.filter(idUser=test01).count())
        if Statisque.objects.filter(idUser=test01).count()!= 0:

            print('CEST BON ')
            inscrit1 = Paiement.objects.get(idUser=test01)
            inscrit = inscrit1.date_debut


            fmts = '%Y-%m-%d'


            stat001 = Statisque.objects.filter(idUser=test01).values('date_heure').last()

            print(' stat001 ')
            print(' stat001 ')
            print(' stat001 ')
            print(' stat001 ')
            print(stat001)

            print(" stat001 ")
            print(stat001['date_heure'])
            print(" inscrit ")
            print(inscrit)

            #inscrit2 = str(inscrit)[:7]
            inscrit2 = str(inscrit)[:10]
            print(" inscrit2 ")
            print(" inscrit2 ")
            print(inscrit2)
            stat000 = stat001['date_heure']
            #stat0000 = str(stat000)[:7]
            stat0000 = str(stat000)[:10]
            print(" stat0000 ")
            print(" stat0000 ")
            print(" stat0000 ")
            print(stat0000)




            stat0011 = datetime.strptime(str(stat0000), fmts)

            inscrit1 = datetime.strptime(str(inscrit2), fmts)
            nombreAnne = stat0011 - inscrit1
            print(nombreAnne)
            nombreAnneA = nombreAnne/365
            print(nombreAnneA)
            print(nombreAnneA)
            print(nombreAnneA)
            print(nombreAnneA)
            print(nombreAnneA)

            #fidelite = Statisque.objects.filter(date_heure__month=1).values('date_heure')

            aneo = datetime.now()
            print(aneo)
            aneo1 = aneo.year-1
            print(aneo1)
            typeAbonnement = utilisateur2.objects.filter(id=test01).values('id_typeabonnement')
            print(' typeAbonnement ')
            print(' typeAbonnement ')
            print(typeAbonnement[0]['id_typeabonnement'])
            print(typeAbonnement)

            if int(typeAbonnement[0]['id_typeabonnement']) == 1 or int(typeAbonnement[0]['id_typeabonnement']) == 6 or int(typeAbonnement[0]['id_typeabonnement']) == 11 or int(typeAbonnement[0]['id_typeabonnement']) == 12 or int(typeAbonnement[0]['id_typeabonnement']) == 13 or int(typeAbonnement[0]['id_typeabonnement']) == 18 or int(typeAbonnement[0]['id_typeabonnement']) == 19:

                fidelite = Statisque.objects.filter(idUser=test01).dates('date_heure', 'month').filter(date_heure__year=aneo1).count()

                if int(fidelite)==12:
                    fidelite1 = Statisque.objects.filter(idUser=test01).dates('date_heure', 'month').filter(date_heure__year=aneo1)
                    valeur = 5
                else:
                    valeur = 0

            elif int(typeAbonnement[0]['id_typeabonnement']) == 4 or int(typeAbonnement[0]['id_typeabonnement']) == 9:

                fidelite = Statisque.objects.filter(idUser=test01).dates('date_heure', 'month').filter(
                    date_heure__year=aneo1).count()

                if int(fidelite) != 0:
                    #fidelite1 = Statisque.objects.filter(idUser=test01).dates('date_heure', 'month').filter(
                        #date_heure__year=aneo1)
                    valeur = 5
                else:
                    valeur = 0

            elif int(typeAbonnement[0]['id_typeabonnement']) == 2 or  int(typeAbonnement[0]['id_typeabonnement']) == 7:

                fidelite = Statisque.objects.filter(idUser=test01).dates('date_heure', 'month').filter(
                    date_heure__year=aneo1).count()

                if int(fidelite) == 12:
                    # fidelite1 = Statisque.objects.filter(idUser=test01).dates('date_heure', 'month').filter(
                    # date_heure__year=aneo1)
                    valeur = 5
                else:
                    valeur = 0

            elif int(typeAbonnement[0]['id_typeabonnement']) == 3 or int(typeAbonnement[0]['id_typeabonnement']) == 8:

                fidelite = Statisque.objects.filter(idUser=test01).dates('date_heure', 'month').filter(
                    date_heure__year=aneo1).count()

                if int(fidelite) == 12:
                    # fidelite1 = Statisque.objects.filter(idUser=test01).dates('date_heure', 'month').filter(
                    # date_heure__year=aneo1)
                    valeur = 5
                else:
                    valeur = 0

            elif int(typeAbonnement[0]['id_typeabonnement']) == 14:

                fidelite = Statisque.objects.filter(idUser=test01).dates('date_heure', 'month').filter(
                    date_heure__year=aneo1).count()

                if int(fidelite) == 12:
                    # fidelite1 = Statisque.objects.filter(idUser=test01).dates('date_heure', 'month').filter(
                    # date_heure__year=aneo1)
                    valeur = 5
                else:
                    valeur = 0

            else:
                valeur = 0

            #elif int(typeAbonnement[0]['id_typeabonnement']) == 2:
            #elif int(typeAbonnement[0]['id_typeabonnement']) == 3:



            print(' fidelite ')
            print(' fidelite ')
            print(' fidelite ')
            print(fidelite)
            print(fidelite)
            #print(fidelite1)
            print(test01)



            #nombreAnneA = nombreAnne.year
            print(" nombreAnne ")
            print(" nombreAnne ")
            print(" nombreAnne ")
            print(str(nombreAnne))

        nbAbonnees = utilisateur2.objects.count()
        nbEssai = personne_essaie.objects.count()

        datedebut = datetime.now()

        datedebut1 = datedebut.strftime("%Y-%m-%d")

        datefin = datetime.now()-timedelta(days=30)
        datefin1 = datefin.strftime("%Y-%m-%d")

        employess = employers.objects.all()
        nbEmployess = employers.objects.count()

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
        #print(abonnesss)

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
        return render(request, 'tables6.html', locals())

def statParSemaine(request):
    if request.session.get('prenom') is None:
        print(' DANS DANS ')
        return render(request, 'login.html')
    else:
        todays = datetime.now()

        employess = employers.objects.all()
        nbEmployess = employers.objects.count()

        stat = Statisque.objects.filter(date_heure__gte=datetime.now()-timedelta(days=7)).values_list('date_heure', 'idUser__nom', 'idUser__prenom', 'id', 'idUser__civilite', 'idUser__civilite').count()

        ##stat = Statisque.objects.filter(date_heure__gte=datetime.now()-timedelta(days=7)).values('date_heure')

        print(" stat stat stat stat stat stat stat stat")
        print(" stat stat stat stat stat stat stat stat")
        print(" stat stat stat stat stat stat stat stat")
        print(" stat stat stat stat stat stat stat stat")
        print(stat)

        stat004 = Statisque.objects.extra(select={'date_heure': 'MONTH(5)'},order_by=['date_heure']).values('id', 'date_heure', 'idUser__nom', 'idUser__prenom')


        #.annotate(count=Count("date_heure"))


        dates = datetime.now()
        formatedDatess = dates.strftime("%Y-%m-%d")
        formatedDatess1 = dates.strftime("%Y")

        return render(request, 'statisque2.html', locals())



def statParJour(request):
    if request.session.get('prenom') is None:
        print(' DANS DANS ')
        return render(request, 'login.html')
    else:
        return render(request, 'tables11.html', locals())



def statParJour1(request):

    if request.session.get('prenom') is None:
        print(' DANS DANS ')
        return render(request, 'login.html')
    else:

        if request.method == "POST":

            dayss = request.POST["jour"]
            print(" DAYS ")
            print(" DAYS ")
            print(" DAYS ")
            print(" DAYS ")
            print(dayss)

            #stat = Statisque.objects.filter(date_heure__gte=datetime.now()-timedelta(days=1)).values('date_heure', 'idUser__nom', 'idUser__prenom', 'id', 'idUser__civilite', 'idUser__civilite').count()
            stat = Statisque.objects.filter(date_heure__contains=dayss).values('date_heure', 'idUser__nom', 'idUser__prenom', 'id', 'idUser__civilite', 'idUser__telephone', 'idUser__email')


            #stat111 = Statisque.objects.filter(date_heure__contains=dayss).values('date_heure', 'idUser__nom', 'idUser__prenom', 'id', 'idUser__civilite', 'idUser__telephone', 'idUser__email')
            ###stat111 = Statisque.objects.filter(date_heure__contains=dayss).annotate(c=Count('id')).dates('date_heure', 'day').annotate(c=Count('date_heure'))
            stat111 = Statisque.objects.filter(date_heure__contains=dayss).annotate(c=Count('id')).extra(select={'hour': 'hour(date_heure)'}).values('hour').annotate(c=Count('id'))


    #dates('date_heure', 'hour').annotate(c=Count('date_heure'))
            print(' stat111 ')
            print(' stat111 ')
            print(' stat111 ')
            print(stat111)
            print(stat111)
            #ordonnees = Statisque.objects.filter(date_heure__range=(start_date, end_date)).annotate(
            #    c=Count('id')).dates('date_heure', 'day').annotate(c=Count('date_heure'))

            print(" stat ")
            print(" stat ")
            print(stat)
            print(stat)

            dates = datetime.now()
            print(stat)
            formatedDatess = dates.strftime("%Y-%m-%d")
            formatedDatess1 = dates.strftime("%Y")

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

            nbAbonnees = utilisateur2.objects.count()
            nbEssai = personne_essaie.objects.count()

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
            #print(abonnesss)

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

            return render(request, 'tables11.html', locals())


def statParMois(request):
    if request.session.get('prenom') is None:
        print(' DANS DANS ')
        return render(request, 'login.html')
    else:

        employess = employers.objects.all()
        nbEmployess = employers.objects.count()
        return render(request, 'tables9.html', locals())



def statCroises(request):
    if request.session.get('prenom') is None:
        print(' DANS DANS ')
        return render(request, 'login.html')
    else:
        employess = employers.objects.all()
        nbEmployess = employers.objects.count()
        return render(request, 'tables13.html', locals())



def statCroises1(request):

    if request.session.get('prenom') is None:
        print(' DANS DANS ')
        return render(request, 'login.html')
    else:

        id_typeabonnement = request.POST['id_typeabonnement']
        annee = request.POST['annee']
        date_du_jour = request.POST['date_du_jour']
        date_de_debut = request.POST['date_de_debut']
        date_de_fin = request.POST['date_de_fin']

        print('date_du_jour')
        print('date_du_jour')
        print('date_du_jour')
        print(date_du_jour)
        print('date_de_debut')
        print('date_de_debut')
        print('date_de_debut')
        print(date_de_debut)
        print('date_de_fin')
        print('date_de_fin')
        print('date_de_fin')
        print(date_de_fin)

        tableau = []
        tableau1 = []
        tableau2 = {}


        if request.method == "POST":

            if id_typeabonnement != "-----" and annee != "-----" and date_du_jour != '' and date_de_debut!='' and date_de_fin!='':

                message = 'Veuillez Sélectionnez soit une date du jour ou bien une date de debut et une date de fin.'

            elif id_typeabonnement != "-----" and annee != "-----" and date_du_jour != '' and date_de_debut=='' and date_de_fin=='':

                stat = Statisque.objects.filter(idUser__id_typeabonnement=id_typeabonnement, date_heure__year=annee, date_heure__contains=date_du_jour).values('date_heure',
                                                                                                    'idUser__nom',
                                                                                                    'idUser__prenom', 'id',
                                                                                                    'idUser__civilite',
                                                                                                    'idUser__telephone',
                                                                                                    'idUser__email')

                #stat111 = Statisque.objects.filter(date_heure__contains=dayss).annotate(c=Count('id')).extra(select={'hour': 'hour(date_heure)'}).values('hour').annotate(c=Count('id'))




            elif id_typeabonnement != "-----" and annee != "-----" and date_du_jour == '' and date_de_debut!='' and date_de_fin!='':

                stat = Statisque.objects.filter(idUser__id_typeabonnement=id_typeabonnement, date_heure__year=annee, date_heure__range=(date_de_debut, date_de_fin)).values('date_heure',
                                                                                                    'idUser__nom',
                                                                                                    'idUser__prenom', 'id',
                                                                                                    'idUser__civilite',
                                                                                                    'idUser__telephone',
                                                                                                    'idUser__email')

                stat111 = Statisque.objects.filter(idUser__id_typeabonnement=id_typeabonnement, date_heure__year=annee, date_heure__range=(date_de_debut, date_de_fin)).annotate(c=Count('id')).extra(select={'hour': 'hour(date_heure)'}).values('hour').annotate(c=Count('id'))

                print(' stat111 ')
                print(' stat111 ')
                print(stat111)
                print(stat111)


            elif id_typeabonnement == "-----" and annee != "-----" and date_du_jour == '' and date_de_debut!='' and date_de_fin!='':

                stat = Statisque.objects.filter(date_heure__year=annee, date_heure__range=(date_de_debut, date_de_fin)).values('date_heure',
                                                                                                    'idUser__nom',
                                                                                                    'idUser__prenom', 'id',
                                                                                                    'idUser__civilite',
                                                                                                    'idUser__telephone',
                                                                                                    'idUser__email')

                stat111 = Statisque.objects.filter(date_heure__year=annee, date_heure__range=(date_de_debut, date_de_fin)).annotate(c=Count('id')).extra(select={'hour': 'hour(date_heure)'}).values('hour').annotate(c=Count('id'))
                print(' stat111 ')
                print(' stat111 ')
                print(stat111)
                print(stat111)


            elif id_typeabonnement == "-----" and annee != "-----" and date_du_jour != '' and date_de_debut == '' and date_de_fin == '':

                stat = Statisque.objects.filter(date_heure__year=annee,
                                                date_heure__contains=date_du_jour).values('date_heure',
                                                                                                       'idUser__nom',
                                                                                                       'idUser__prenom',
                                                                                                       'id',
                                                                                                       'idUser__civilite',
                                                                                                       'idUser__telephone',
                                                                                                       'idUser__email')
            elif id_typeabonnement != "-----" and annee != "-----" and date_du_jour == '' and date_de_debut =='' and date_de_fin=='':

                stat = Statisque.objects.filter(idUser__id_typeabonnement=id_typeabonnement, date_heure__year=annee).values('date_heure', 'idUser__nom',
                                                                                   'idUser__prenom', 'id',
                                                                                   'idUser__civilite', 'idUser__telephone',
                                                                                   'idUser__email')
                print("COOL ")
                print("COOL ")
                print(stat)



            elif id_typeabonnement != "-----" and annee == "-----" and date_du_jour != '' and date_de_debut =='' and date_de_fin=='':

                stat = Statisque.objects.filter(idUser__id_typeabonnement=id_typeabonnement, date_heure__contains=date_du_jour).values('date_heure',
                                                                                                    'idUser__nom',
                                                                                                    'idUser__prenom', 'id',
                                                                                                    'idUser__civilite',
                                                                                                    'idUser__telephone',
                                                                                                    'idUser__email')


            elif id_typeabonnement != "-----" and annee == "-----" and date_du_jour == '' and date_de_debut !='' and date_de_fin!='':

                stat = Statisque.objects.filter(idUser__id_typeabonnement=id_typeabonnement, date_heure__range=(date_de_debut, date_de_fin)).values('date_heure',
                                                                                                    'idUser__nom',
                                                                                                    'idUser__prenom', 'id',
                                                                                                    'idUser__civilite',
                                                                                                    'idUser__telephone',
                                                                                                    'idUser__email')

                stat111 = Statisque.objects.filter(idUser__id_typeabonnement=id_typeabonnement, date_heure__range=(date_de_debut, date_de_fin)).annotate(c=Count('id')).extra(select={'hour': 'hour(date_heure)'}).values('hour').annotate(c=Count('id'))
                print(' stat111 ')
                print(' stat111 ')
                print(stat111)
                print(stat111)

            elif id_typeabonnement != "-----" and annee == "-----" and date_du_jour =='' and date_de_debut =='' and date_de_fin=='':

                stat = Statisque.objects.filter(idUser__id_typeabonnement=id_typeabonnement).values('date_heure',
                                                                                                    'idUser__nom',
                                                                                                    'idUser__prenom', 'id',
                                                                                                    'idUser__civilite',
                                                                                                    'idUser__telephone',
                                                                                                    'idUser__email')

            elif id_typeabonnement == "-----" and annee != "-----" and date_du_jour == ''  and date_de_debut =='' and date_de_fin=='':
                stat = Statisque.objects.filter(date_heure__year=annee).values('date_heure',
                                                                               'idUser__nom',
                                                                               'idUser__prenom', 'id',
                                                                               'idUser__civilite',
                                                                               'idUser__telephone',
                                                                               'idUser__email')

            elif id_typeabonnement == "-----" and annee == "-----" and date_du_jour != '' and date_de_debut =='' and date_de_fin=='':
                stat = Statisque.objects.filter(date_heure__contains=date_du_jour).values('date_heure',
                                                                               'idUser__nom',
                                                                               'idUser__prenom', 'id',
                                                                               'idUser__civilite',
                                                                               'idUser__telephone',
                                                                               'idUser__email')

            elif id_typeabonnement == "-----" and annee == "-----" and date_du_jour == '' and date_de_debut !='' and date_de_fin!='':
                stat = Statisque.objects.filter(date_heure__range=(date_de_debut, date_de_fin)).values('date_heure',
                                                                                          'idUser__nom',
                                                                                          'idUser__prenom', 'id',
                                                                                          'idUser__civilite',
                                                                                          'idUser__telephone',
                                                                                          'idUser__email')

                stat111 = Statisque.objects.filter(date_heure__range=(date_de_debut, date_de_fin)).annotate(
                    c=Count('id')).extra(select={'hour': 'hour(date_heure)'}).values('hour').annotate(c=Count('id'))
                print(' stat111 ')
                print(' stat111 ')
                print(stat111)
                print(stat111)

                abscisse = Statisque.objects.filter(date_heure__range=(date_de_debut, date_de_fin)).dates('date_heure', 'day')
                print(' ABSCISSE ')
                print(' ABSCISSE ')
                print(abscisse)

                ordonnees = Statisque.objects.filter(date_heure__range=(date_de_debut, date_de_fin)).annotate(
                    c=Count('id')).dates('date_heure', 'day').annotate(c=Count('date_heure'))


                abscisseHeb = Statisque.objects.filter(date_heure__range=(date_de_debut, date_de_fin)).dates('date_heure', 'day')
                print(' abscisseHeb ')
                print(' abscisseHeb ')
                print(abscisseHeb)
                #abscisseHeb4 = Statisque.objects.filter(date_heure__range=(date_de_debut, date_de_fin)).annotate(c=Count('id')).annotate(c=Count('date_heure')).dates('date_heure', 'day')
                abscisseHeb4 = Statisque.objects.filter(date_heure__range=(date_de_debut, date_de_fin)).annotate(
                    #c=Count('id')).extra(select={'date_heure': 'day(date_heure)'}).values('date_heure').annotate(c=Count('id'))
                    c=Count('id')).extra(select={'date_heure': "DATE_FORMAT(date_heure, '%%Y-%%m-%%d')"}).values('date_heure').annotate(c=Count('id'))
                print(' abscisseHeb 4')
                print(' abscisseHeb 4')
                print(' abscisseHeb 4')
                print(abscisseHeb4)

                abscisseHeb5 = Statisque.objects.filter(date_heure__range=(date_de_debut, date_de_fin)).annotate(c=Count('id')).extra(select={'date_heure': "DATE_FORMAT(date_heure, '%%Y-%%m-%%d')"}).values('date_heure').annotate(c=Count('id')).annotate(moyenne=Count('id')/Count('idUser', distinct=True))
                print(abscisseHeb5)


                for abscisseHeb001 in abscisseHeb5:

                    leJoursssss = datetime.strptime(str(abscisseHeb001['date_heure']), "%Y-%m-%d")
                    leJour = calendar.day_name[leJoursssss.weekday()]

                    if leJour in tableau2:

                        tableau2[leJour] = tableau2[leJour]+abscisseHeb001['moyenne']

                    else:
                        tableau2[leJour] = abscisseHeb001['moyenne']



                print(' FIN DE LA BOUCLE 1')
                print(' FIN DE LA BOUCLE 2')
                print(' FIN DE LA BOUCLE 3')
                print(tableau2)
                ordonneesHeb = Statisque.objects.filter(date_heure__range=(date_de_debut, date_de_fin)).annotate(
                    c=Count('id')).dates('date_heure', 'day').annotate(c=Count('date_heure'))

                print(' ordonneesHeb ')
                print(' ordonneesHeb ')
                print(ordonneesHeb)


                statByMois = Statisque.objects.extra({'date_heure':"MONTH(date_heure)"}).values('date_heure').annotate(moyenne=Count('id')/Count('idUser', distinct=True))

                statMensss = Statisque.objects.filter(date_heure__range=(date_de_debut, date_de_fin)).annotate(
                    c=Count('id')).extra(select={'hour': 'hour(date_heure)'}).\
                    extra(select={'date_heure': "DATE_FORMAT(date_heure, '%%Y-%%m-%%d')"}).values('hour','date_heure').annotate(c=Count('id'))

                #extra(select={'date_heure': "DATE_FORMAT(date_heure, '%%Y-%%m-%%d')"}).values('hour', 'date_heure').annotate(c=Count('id'))

                print(' statMensss ')
                print(' statMensss ')
                print(' statMensss ')
                print(statMensss)


                #abscisseHeb4 = Statisque.objects.filter(date_heure__range=(date_de_debut, date_de_fin)).annotate(
                #    c=Count('id')).extra(select={'date_heure': "DATE_FORMAT(date_heure, '%%Y-%%m-%%d')"}).values(
                #    'date_heure').annotate(c=Count('id'))


            return render(request, 'tables13.html', locals())


def statParMoisForms(request):

    if request.session.get('prenom') is None:
        print(' DANS DANS ')
        return render(request, 'login.html')
    else:


        if request.method == "POST":
            start_date = ""
            end_date = ""
            mois = request.POST["mois"]

            print(" mois ")
            print(" mois ")
            print(" mois ")
            print(mois)




            if int(mois)==4:

                print(" DANS LE MOIS 4")
                start_date = "2018-04-01"
                end_date = "2018-05-01"
                stat = Statisque.objects.filter(date_heure__range=(start_date, end_date)).values('date_heure', 'idUser__nom',
                                                                                                 'idUser__prenom', 'id',
                                                                                                 'idUser__civilite',
                                                                                                 'idUser__civilite')

                print(stat)

                abscisse = Statisque.objects.filter(date_heure__range=(start_date, end_date)).dates('date_heure', 'day')
                ordonnees = Statisque.objects.filter(date_heure__range=(start_date, end_date)).annotate(
                    c=Count('id')).dates('date_heure', 'day').annotate(c=Count('date_heure'))
                print(' ABCISSE ')
                print(' ABCISSE ')
                print(' ABCISSE ')
                print(abscisse)
                print(' ordonnees ')
                print(' ordonnees ')
                print(' ordonnees ')
                print(' ordonnees ')
                print(ordonnees)

            elif int(mois) == 5:
                start_date = "2018-05-01"
                end_date = "2018-06-01"
                stat = Statisque.objects.filter(date_heure__range=(start_date, end_date)).values('date_heure', 'idUser__nom',
                                                                                                 'idUser__prenom', 'id',
                                                                                                 'idUser__civilite',
                                                                                                 'idUser__civilite')


                abscisse = Statisque.objects.filter(date_heure__range=(start_date, end_date)).dates('date_heure', 'day')
                ordonnees = Statisque.objects.filter(date_heure__range=(start_date, end_date)).annotate(
                    c=Count('id')).dates('date_heure', 'day').annotate(c=Count('date_heure'))
                print(' ABCISSE ')
                print(' ABCISSE ')
                print(' ABCISSE ')
                print(abscisse)
                print(' ordonnees ')
                print(' ordonnees ')
                print(' ordonnees ')
                print(' ordonnees ')
                print(ordonnees)

            elif int(mois) == 6:
                start_date = "2018-06-01"
                end_date = "2018-07-01"
                stat = Statisque.objects.filter(date_heure__range=(start_date, end_date)).values('date_heure', 'idUser__nom',
                                                                                                 'idUser__prenom', 'id',
                                                                                                 'idUser__civilite',
                                                                                                 'idUser__civilite')

                abscisse = Statisque.objects.filter(date_heure__range=(start_date, end_date)).dates('date_heure', 'day')
                ordonnees = Statisque.objects.filter(date_heure__range=(start_date, end_date)).annotate(
                    c=Count('id')).dates('date_heure', 'day').annotate(c=Count('date_heure'))
                print(' ABCISSE ')
                print(' ABCISSE ')
                print(' ABCISSE ')
                print(abscisse)
                print(' ordonnees ')
                print(' ordonnees ')
                print(' ordonnees ')
                print(' ordonnees ')
                print(ordonnees)



            elif int(mois) == 7:
                start_date = "2018-07-01"
                end_date = "2018-08-01"
                stat = Statisque.objects.filter(date_heure__range=(start_date, end_date)).values('date_heure', 'idUser__nom',
                                                                                                 'idUser__prenom', 'id',
                                                                                                 'idUser__civilite',
                                                                                                 'idUser__civilite')

                abscisse = Statisque.objects.filter(date_heure__range=(start_date, end_date)).dates('date_heure', 'day')
                ordonnees = Statisque.objects.filter(date_heure__range=(start_date, end_date)).annotate(
                    c=Count('id')).dates('date_heure', 'day').annotate(c=Count('date_heure'))
                print(' ABCISSE ')
                print(' ABCISSE ')
                print(' ABCISSE ')
                print(abscisse)
                print(' ordonnees ')
                print(' ordonnees ')
                print(' ordonnees ')
                print(' ordonnees ')
                print(ordonnees)

            elif int(mois) == 8:
                start_date = "2018-08-01"
                end_date = "2018-09-01"
                stat = Statisque.objects.filter(date_heure__range=(start_date, end_date)).values('date_heure', 'idUser__nom',
                                                                                                 'idUser__prenom', 'id',
                                                                                                 'idUser__civilite',
                                                                                                 'idUser__civilite')

                abscisse = Statisque.objects.filter(date_heure__range=(start_date, end_date)).dates('date_heure', 'day')
                ordonnees = Statisque.objects.filter(date_heure__range=(start_date, end_date)).annotate(
                    c=Count('id')).dates('date_heure', 'day').annotate(c=Count('date_heure'))
                print(' ABCISSE ')
                print(' ABCISSE ')
                print(' ABCISSE ')
                print(abscisse)
                print(' ordonnees ')
                print(' ordonnees ')
                print(' ordonnees ')
                print(' ordonnees ')
                print(ordonnees)

            elif int(mois) == 9:
                start_date = "2018-09-01"
                end_date = "2018-10-01"
                stat = Statisque.objects.filter(date_heure__range=(start_date, end_date)).values('date_heure', 'idUser__nom',
                                                                                                 'idUser__prenom', 'id',
                                                                                                 'idUser__civilite',
                                                                                                 'idUser__civilite')

                abscisse = Statisque.objects.filter(date_heure__range=(start_date, end_date)).dates('date_heure', 'day')
                ordonnees = Statisque.objects.filter(date_heure__range=(start_date, end_date)).annotate(
                    c=Count('id')).dates('date_heure', 'day').annotate(c=Count('date_heure'))
                print(' ABCISSE ')
                print(' ABCISSE ')
                print(' ABCISSE ')
                print(abscisse)
                print(' ordonnees ')
                print(' ordonnees ')
                print(' ordonnees ')
                print(' ordonnees ')
                print(ordonnees)

            elif int(mois) == 10:
                start_date = "2018-10-01"
                end_date = "2018-11-01"
                stat = Statisque.objects.filter(date_heure__range=(start_date, end_date)).values('date_heure', 'idUser__nom',
                                                                                                 'idUser__prenom', 'id',
                                                                                                 'idUser__civilite',
                                                                                                 'idUser__civilite')

                abscisse = Statisque.objects.filter(date_heure__range=(start_date, end_date)).dates('date_heure', 'day')
                ordonnees = Statisque.objects.filter(date_heure__range=(start_date, end_date)).annotate(
                    c=Count('id')).dates('date_heure', 'day').annotate(c=Count('date_heure'))
                print(' ABCISSE ')
                print(' ABCISSE ')
                print(' ABCISSE ')
                print(abscisse)
                print(' ordonnees ')
                print(' ordonnees ')
                print(' ordonnees ')
                print(' ordonnees ')
                print(ordonnees)

            elif int(mois) == 11:
                start_date = "2018-11-01"
                end_date = "2018-12-01"
                stat = Statisque.objects.filter(date_heure__range=(start_date, end_date)).values('date_heure', 'idUser__nom',
                                                                                                 'idUser__prenom', 'id',
                                                                                                 'idUser__civilite',
                                                                                                 'idUser__civilite')

                abscisse = Statisque.objects.filter(date_heure__range=(start_date, end_date)).dates('date_heure', 'day')
                ordonnees = Statisque.objects.filter(date_heure__range=(start_date, end_date)).annotate(
                    c=Count('id')).dates('date_heure', 'day').annotate(c=Count('date_heure'))
                print(' ABCISSE ')
                print(' ABCISSE ')
                print(' ABCISSE ')
                print(abscisse)
                print(' ordonnees ')
                print(' ordonnees ')
                print(' ordonnees ')
                print(' ordonnees ')
                print(ordonnees)

            elif int(mois) == 12:
                start_date = "2018-12-01"
                end_date = "2019-01-01"
                stat = Statisque.objects.filter(date_heure__range=(start_date, end_date)).values('date_heure', 'idUser__nom',
                                                                                                 'idUser__prenom', 'id',
                                                                                                 'idUser__civilite',
                                                                                                 'idUser__civilite')
                abscisse = Statisque.objects.filter(date_heure__range=(start_date, end_date)).dates('date_heure', 'day')
                ordonnees = Statisque.objects.filter(date_heure__range=(start_date, end_date)).annotate(
                    c=Count('id')).dates('date_heure', 'day').annotate(c=Count('date_heure'))
                print(' ABCISSE ')
                print(' ABCISSE ')
                print(' ABCISSE ')
                print(abscisse)
                print(' ordonnees ')
                print(' ordonnees ')
                print(' ordonnees ')
                print(' ordonnees ')
                print(ordonnees)

            elif int(mois) == 1:
                start_date = "2018-01-01"
                end_date = "2018-02-01"
                stat = Statisque.objects.filter(date_heure__range=(start_date, end_date)).values('date_heure', 'idUser__nom',
                                                                                                 'idUser__prenom', 'id',
                                                                                                 'idUser__civilite',
                                                                                                 'idUser__civilite')

                abscisse = Statisque.objects.filter(date_heure__range=(start_date, end_date)).dates('date_heure', 'day')
                ordonnees = Statisque.objects.filter(date_heure__range=(start_date, end_date)).annotate(
                    c=Count('id')).dates('date_heure', 'day').annotate(c=Count('date_heure'))
                print(' ABCISSE ')
                print(' ABCISSE ')
                print(' ABCISSE ')
                print(abscisse)
                print(' ordonnees ')
                print(' ordonnees ')
                print(' ordonnees ')
                print(' ordonnees ')
                print(ordonnees)

            elif int(mois) == 2:
                start_date = "2018-02-01"
                end_date = "2018-03-01"
                stat = Statisque.objects.filter(date_heure__range=(start_date, end_date)).values('date_heure', 'idUser__nom',
                                                                                                 'idUser__prenom', 'id',
                                                                                                 'idUser__civilite',
                                                                                                 'idUser__civilite')
                abscisse = Statisque.objects.filter(date_heure__range=(start_date, end_date)).dates('date_heure', 'day')
                ordonnees = Statisque.objects.filter(date_heure__range=(start_date, end_date)).annotate(
                    c=Count('id')).dates('date_heure', 'day').annotate(c=Count('date_heure'))
                print(' ABCISSE ')
                print(' ABCISSE ')
                print(' ABCISSE ')
                print(abscisse)
                print(' ordonnees ')
                print(' ordonnees ')
                print(' ordonnees ')
                print(' ordonnees ')
                print(ordonnees)
                #else mois == 3:
            elif int(mois) == 3:
                start_date = "2018-03-01"
                end_date = "2018-04-01"
                stat = Statisque.objects.filter(date_heure__range=(start_date, end_date)).values('date_heure', 'idUser__nom',
                                                                                                 'idUser__prenom', 'id',
                                                                                                 'idUser__civilite',
                                                                                                 'idUser__civilite')

                abscisse = Statisque.objects.filter(date_heure__range=(start_date, end_date)).dates('date_heure', 'day')
                ordonnees = Statisque.objects.filter(date_heure__range=(start_date, end_date)).annotate(
                    c=Count('id')).dates('date_heure', 'day').annotate(c=Count('date_heure'))
                print(' ABCISSE ')
                print(' ABCISSE ')
                print(' ABCISSE ')
                print(abscisse)
                print(' ordonnees ')
                print(' ordonnees ')
                print(' ordonnees ')
                print(' ordonnees ')
                print(ordonnees)

            elif int(mois) == 13:
                start_date = "2019-01-01"
                end_date = "2019-02-01"
                stat = Statisque.objects.filter(date_heure__range=(start_date, end_date)).values('date_heure', 'idUser__nom',
                                                                                                 'idUser__prenom', 'id',
                                                                                                 'idUser__civilite',
                                                                                                 'idUser__civilite')

                abscisse = Statisque.objects.filter(date_heure__range=(start_date, end_date)).dates('date_heure', 'day')
                ordonnees = Statisque.objects.filter(date_heure__range=(start_date, end_date)).annotate(
                    c=Count('id')).dates('date_heure', 'day').annotate(c=Count('date_heure'))
                print(' ABCISSE ')
                print(' ABCISSE ')
                print(' ABCISSE ')
                print(abscisse)
                print(' ordonnees ')
                print(' ordonnees ')
                print(' ordonnees ')
                print(' ordonnees ')
                print(ordonnees)

            elif int(mois) == 14:
                start_date = "2019-02-01"
                end_date = "2019-03-01"
                stat = Statisque.objects.filter(date_heure__range=(start_date, end_date)).values('date_heure', 'idUser__nom',
                                                                                                 'idUser__prenom', 'id',
                                                                                                 'idUser__civilite',
                                                                                                 'idUser__civilite')

                abscisse = Statisque.objects.filter(date_heure__range=(start_date, end_date)).dates('date_heure', 'day')
                ordonnees = Statisque.objects.filter(date_heure__range=(start_date, end_date)).annotate(
                    c=Count('id')).dates('date_heure', 'day').annotate(c=Count('date_heure'))
                print(' ABCISSE ')
                print(' ABCISSE ')
                print(' ABCISSE ')
                print(abscisse)
                print(' ordonnees ')
                print(' ordonnees ')
                print(' ordonnees ')
                print(' ordonnees ')
                print(ordonnees)
            elif int(mois) == 15:
                start_date = "2019-03-01"
                end_date = "2019-04-01"
                stat = Statisque.objects.filter(date_heure__range=(start_date, end_date)).values('date_heure', 'idUser__nom',
                                                                                                 'idUser__prenom', 'id',
                                                                                                 'idUser__civilite',
                                                                                                 'idUser__civilite')

                abscisse = Statisque.objects.filter(date_heure__range=(start_date, end_date)).dates('date_heure', 'day')
                ordonnees = Statisque.objects.filter(date_heure__range=(start_date, end_date)).annotate(
                    c=Count('id')).dates('date_heure', 'day').annotate(c=Count('date_heure'))
                print(' ABCISSE ')
                print(' ABCISSE ')
                print(' ABCISSE ')
                print(abscisse)
                print(' ordonnees ')
                print(' ordonnees ')
                print(' ordonnees ')
                print(' ordonnees ')
                print(ordonnees)

            elif int(mois) == 16:
                start_date = "2019-04-01"
                end_date = "2019-05-01"
                stat = Statisque.objects.filter(date_heure__range=(start_date, end_date)).values('date_heure', 'idUser__nom',
                                                                                                 'idUser__prenom', 'id',
                                                                                                 'idUser__civilite',
                                                                                                 'idUser__civilite')

                abscisse = Statisque.objects.filter(date_heure__range=(start_date, end_date)).dates('date_heure', 'day')
                ordonnees = Statisque.objects.filter(date_heure__range=(start_date, end_date)).annotate(
                    c=Count('id')).dates('date_heure', 'day').annotate(c=Count('date_heure'))
                print(' ABCISSE ')
                print(' ABCISSE ')
                print(' ABCISSE ')
                print(abscisse)
                print(' ordonnees ')
                print(' ordonnees ')
                print(' ordonnees ')
                print(' ordonnees ')
                print(ordonnees)
            elif int(mois) == 17:
                start_date = "2019-05-01"
                end_date = "2019-06-01"
                stat = Statisque.objects.filter(date_heure__range=(start_date, end_date)).values('date_heure', 'idUser__nom',
                                                                                                 'idUser__prenom', 'id',
                                                                                                 'idUser__civilite',
                                                                                                 'idUser__civilite')

                abscisse = Statisque.objects.filter(date_heure__range=(start_date, end_date)).dates('date_heure', 'day')
                ordonnees = Statisque.objects.filter(date_heure__range=(start_date, end_date)).annotate(
                    c=Count('id')).dates('date_heure', 'day').annotate(c=Count('date_heure'))
                print(' ABCISSE ')
                print(' ABCISSE ')
                print(' ABCISSE ')
                print(abscisse)
                print(' ordonnees ')
                print(' ordonnees ')
                print(' ordonnees ')
                print(' ordonnees ')
                print(ordonnees)

            elif int(mois) == 18:
                start_date = "2019-06-01"
                end_date = "2019-07-01"
                stat = Statisque.objects.filter(date_heure__range=(start_date, end_date)).values('date_heure', 'idUser__nom',
                                                                                                 'idUser__prenom', 'id',
                                                                                                 'idUser__civilite',
                                                                                                 'idUser__civilite')

                abscisse = Statisque.objects.filter(date_heure__range=(start_date, end_date)).dates('date_heure', 'day')
                ordonnees = Statisque.objects.filter(date_heure__range=(start_date, end_date)).annotate(
                    c=Count('id')).dates('date_heure', 'day').annotate(c=Count('date_heure'))
                print(' ABCISSE ')
                print(' ABCISSE ')
                print(' ABCISSE ')
                print(abscisse)
                print(' ordonnees ')
                print(' ordonnees ')
                print(' ordonnees ')
                print(' ordonnees ')
                print(ordonnees)

            elif int(mois) == 19:
                start_date = "2019-07-01"
                end_date = "2019-08-01"
                stat = Statisque.objects.filter(date_heure__range=(start_date, end_date)).values('date_heure', 'idUser__nom',
                                                                                                 'idUser__prenom', 'id',
                                                                                                 'idUser__civilite',
                                                                                                 'idUser__civilite')

                abscisse = Statisque.objects.filter(date_heure__range=(start_date, end_date)).dates('date_heure', 'day')
                ordonnees = Statisque.objects.filter(date_heure__range=(start_date, end_date)).annotate(
                    c=Count('id')).dates('date_heure', 'day').annotate(c=Count('date_heure'))
                print(' ABCISSE ')
                print(' ABCISSE ')
                print(' ABCISSE ')
                print(abscisse)
                print(' ordonnees ')
                print(' ordonnees ')
                print(' ordonnees ')
                print(' ordonnees ')
                print(ordonnees)

            elif int(mois) == 20:
                start_date = "2019-08-01"
                end_date = "2019-09-01"
                stat = Statisque.objects.filter(date_heure__range=(start_date, end_date)).values('date_heure', 'idUser__nom',
                                                                                                 'idUser__prenom', 'id',
                                                                                                 'idUser__civilite',
                                                                                                 'idUser__civilite')

                abscisse = Statisque.objects.filter(date_heure__range=(start_date, end_date)).dates('date_heure', 'day')
                ordonnees = Statisque.objects.filter(date_heure__range=(start_date, end_date)).annotate(
                    c=Count('id')).dates('date_heure', 'day').annotate(c=Count('date_heure'))
                print(' ABCISSE ')
                print(' ABCISSE ')
                print(' ABCISSE ')
                print(abscisse)
                print(' ordonnees ')
                print(' ordonnees ')
                print(' ordonnees ')
                print(' ordonnees ')
                print(ordonnees)

            elif int(mois) == 21:
                start_date = "2019-09-01"
                end_date = "2019-10-01"
                stat = Statisque.objects.filter(date_heure__range=(start_date, end_date)).values('date_heure', 'idUser__nom',
                                                                                                 'idUser__prenom', 'id',
                                                                                                 'idUser__civilite',
                                                                                                 'idUser__civilite')

                abscisse = Statisque.objects.filter(date_heure__range=(start_date, end_date)).dates('date_heure', 'day')
                ordonnees = Statisque.objects.filter(date_heure__range=(start_date, end_date)).annotate(
                    c=Count('id')).dates('date_heure', 'day').annotate(c=Count('date_heure'))
                print(' ABCISSE ')
                print(' ABCISSE ')
                print(' ABCISSE ')
                print(abscisse)
                print(' ordonnees ')
                print(' ordonnees ')
                print(' ordonnees ')
                print(' ordonnees ')
                print(ordonnees)

            elif int(mois) == 22:
                start_date = "2019-10-01"
                end_date = "2019-11-01"
                stat = Statisque.objects.filter(date_heure__range=(start_date, end_date)).values('date_heure', 'idUser__nom',
                                                                                                 'idUser__prenom', 'id',
                                                                                                 'idUser__civilite',
                                                                                                 'idUser__civilite')

                abscisse = Statisque.objects.filter(date_heure__range=(start_date, end_date)).dates('date_heure', 'day')
                ordonnees = Statisque.objects.filter(date_heure__range=(start_date, end_date)).annotate(
                    c=Count('id')).dates('date_heure', 'day').annotate(c=Count('date_heure'))
                print(' ABCISSE ')
                print(' ABCISSE ')
                print(' ABCISSE ')
                print(abscisse)
                print(' ordonnees ')
                print(' ordonnees ')
                print(' ordonnees ')
                print(' ordonnees ')
                print(ordonnees)

            elif int(mois) == 23:
                start_date = "2019-11-01"
                end_date = "2019-12-01"
                stat = Statisque.objects.filter(date_heure__range=(start_date, end_date)).values('date_heure', 'idUser__nom',
                                                                                                 'idUser__prenom', 'id',
                                                                                                 'idUser__civilite',
                                                                                                 'idUser__civilite')

                abscisse = Statisque.objects.filter(date_heure__range=(start_date, end_date)).dates('date_heure', 'day')
                ordonnees = Statisque.objects.filter(date_heure__range=(start_date, end_date)).annotate(
                    c=Count('id')).dates('date_heure', 'day').annotate(c=Count('date_heure'))
                print(' ABCISSE ')
                print(' ABCISSE ')
                print(' ABCISSE ')
                print(abscisse)
                print(' ordonnees ')
                print(' ordonnees ')
                print(' ordonnees ')
                print(' ordonnees ')
                print(ordonnees)
            elif int(mois) == 24:
                start_date = "2019-12-01"
                end_date = "2020-01-01"
                stat = Statisque.objects.filter(date_heure__range=(start_date, end_date)).values('date_heure', 'idUser__nom',
                                                                                                 'idUser__prenom', 'id',
                                                                                                 'idUser__civilite',
                                                                                                 'idUser__civilite')

                abscisse = Statisque.objects.filter(date_heure__range=(start_date, end_date)).dates('date_heure', 'day')
                ordonnees = Statisque.objects.filter(date_heure__range=(start_date, end_date)).annotate(
                    c=Count('id')).dates('date_heure', 'day').annotate(c=Count('date_heure'))
                print(' ABCISSE ')
                print(' ABCISSE ')
                print(' ABCISSE ')
                print(abscisse)
                print(' ordonnees ')
                print(' ordonnees ')
                print(' ordonnees ')
                print(' ordonnees ')
                print(ordonnees)









            print("LA VALEUR ")
            #print(start_date)
            #print(end_date)

            nbAbonnees = utilisateur2.objects.count()
            nbEssai = personne_essaie.objects.count()

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
            #print(abonnesss)

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

            return render(request, 'tables9.html', locals())
        return render(request, 'tables9.html', locals())


def statParMois30derniersJours(request):

    if request.session.get('prenom') is None:
        print(' DANS DANS ')
        return render(request, 'login.html')
    else:

        #stat = Statisque.objects.filter(date_heure__gte=datetime.now()-timedelta(days=30)).values_list('date_heure', 'idUser__nom', 'idUser__prenom', 'id', 'idUser__civilite', 'idUser__civilite')
        stat = Statisque.objects.extra({'idUser':'idUser'}).filter(date_heure__gte=datetime.now()-timedelta(days=30)).values_list('date_heure', 'idUser__nom', 'idUser__prenom', 'id', 'idUser__civilite', 'idUser__civilite').count(idUser=Count('idUser__id'))
        print(" stat stat stat stat stat stat stat stat stat stat stat")
        print(" stat stat stat stat stat stat stat stat stat stat stat")
        print(" stat stat stat stat stat stat stat stat stat stat stat")
        print(" stat stat stat stat stat stat stat stat stat stat stat")
        print(stat)
        print(" stat.count() stat.count() stat.count() stat.count() stat.count()")
        print(" stat.count() stat.count() stat.count() stat.count() stat.count()")
        print(" stat.count() stat.count() stat.count() stat.count() stat.count()")
        print(" stat.count() stat.count() stat.count() stat.count() stat.count()")
        print(stat.count())
        stat1 = Statisque.objects.filter(date_heure__gte=datetime.now()-timedelta(days=30))
        print(" stat1 stat1 stat1 stat1 stat1 stat1 stat1 stat1 stat1 stat1")
        print(" stat1 stat1 stat1 stat1 stat1 stat1 stat1 stat1 stat1 stat1")
        print(" stat1 stat1 stat1 stat1 stat1 stat1 stat1 stat1 stat1 stat1")
        print(" stat1 stat1 stat1 stat1 stat1 stat1 stat1 stat1 stat1 stat1")
        print(stat1)
        nombre = Statisque.objects.annotate(nbAbonne=Count("idUser")).filter(date_heure__gte=datetime.now()-timedelta(days=30))
        print("NOMBRE NOMBRE NOMBRE NOMBRE NOMBRE NOMBRE")
        print("NOMBRE NOMBRE NOMBRE NOMBRE NOMBRE NOMBRE")
        print("NOMBRE NOMBRE NOMBRE NOMBRE NOMBRE NOMBRE")
        print(nombre)
        #p = Product.objects.annotate(nb_items=Count("product_item")).get(pk=1)
        #p.nb_items
        return render(request, 'statisque1.html', locals())



def statHeuresdaff(request):
    if request.session.get('prenom') is None:
        print(' DANS DANS ')
        return render(request, 'login.html')
    else:

        stat = Statisque.objects.extra(select={'heure_daff':'date(date_heure)'}).values_list('heure_daff').annotate(max_date=Max('date_heure'))
        print(stat)
        return render(request, 'statisque1.html', locals())


def hebdomadaires(request):

    if request.session.get('prenom') is None:
        print(' DANS DANS ')
        return render(request, 'login.html')
    else:
        return render(request, 'tables12.html', locals())

def hebdomadaires1(request):

    if request.session.get('prenom') is None:
        print(' DANS DANS ')
        return render(request, 'login.html')
    else:

        if request.method == "POST":
            #start_date = request.POST['date_de_debut']
            #end_date = request.POST['date_de_fin']
            #stat = Statisque.objects.filter(date_heure__range=(start_date, end_date)).values('id', 'date_heure', 'idUser',
            #                                                                                 'idUser__nom',
            #                                                                                 'idUser__prenom',
            #                                                                                 'idUser__civilite',
            #                                                                                 'idUser__dateNaiss')
            #print(stat)

            print(" request.POST['semaine'] ")
            print(" request.POST['semaine'] ")
            print(request.POST['semaine'])
            print(request.POST['semaine'])

            if int(request.POST['semaine']) == 1:

                start_date = "2018-01-01"
                end_date = "2018-01-08"
                stat = Statisque.objects.filter(date_heure__range=(start_date, end_date)).values('id', 'date_heure', 'idUser',
                                                                                                 'idUser__nom',
                                                                                                 'idUser__prenom',
                                                                                                 'idUser__civilite',
                                                                                                 'idUser__dateNaiss')

                #stat01 = Statisque.objects.filter(date_heure__range=(start_date, end_date)).annotate(dcount=Count('date_heure')).dates('date_heure', 'day').annotate(c=Count('id'))

                abscisse = Statisque.objects.filter(date_heure__range=(start_date, end_date)).dates('date_heure', 'day')
                ordonnees = Statisque.objects.filter(date_heure__range=(start_date, end_date)).annotate(c=Count('id')).dates('date_heure', 'day').annotate(c=Count('date_heure'))
                print(' abscisse ')
                print(' abscisse ')
                print(abscisse)
                print(abscisse)
                print(' ordonnees ')
                print(' ordonnees ')
                print(ordonnees)
                print(ordonnees)

                stat0001 = Statisque.objects.extra(
                        select={
                            'valeur': "SELECT *, COUNT(date_heure) FROM users_statisque GROUP BY date_heure"
                        }
                    )


                stat02 = Statisque.objects.values('date_heure').annotate(dcount=Count('date_heure')).filter(date_heure__range=(start_date, end_date))
                print(' stat02 ')
                print(' stat02 ')
                print(' stat02 ')
                print(stat02)
                print(stat02)

            elif int(request.POST['semaine']) == 2:
                start_date = "2018-01-08"
                end_date = "2018-01-15"
                stat = Statisque.objects.filter(date_heure__range=(start_date, end_date)).values('id', 'date_heure',
                                                                                                 'idUser',
                                                                                                 'idUser__nom',
                                                                                                 'idUser__prenom',
                                                                                                 'idUser__civilite',
                                                                                                 'idUser__dateNaiss')

                # stat01 = Statisque.objects.filter(date_heure__range=(start_date, end_date)).annotate(dcount=Count('date_heure')).dates('date_heure', 'day').annotate(c=Count('id'))

                abscisse = Statisque.objects.filter(date_heure__range=(start_date, end_date)).dates('date_heure', 'day')
                ordonnees = Statisque.objects.filter(date_heure__range=(start_date, end_date)).annotate(
                    c=Count('id')).dates('date_heure', 'day').annotate(c=Count('date_heure'))
                print(' abscisse ')
                print(' abscisse ')
                print(abscisse)
                print(abscisse)
                print(' ordonnees ')
                print(' ordonnees ')
                print(ordonnees)
                print(ordonnees)

                stat0001 = Statisque.objects.extra(
                    select={
                        'valeur': "SELECT *, COUNT(date_heure) FROM users_statisque GROUP BY date_heure"
                    }
                )

                stat02 = Statisque.objects.values('date_heure').annotate(dcount=Count('date_heure')).filter(
                    date_heure__range=(start_date, end_date))
                print(' stat02 ')
                print(' stat02 ')
                print(' stat02 ')
                print(stat02)
                print(stat02)

            elif int(request.POST['semaine']) == 3:
                start_date = "2018-01-15"
                end_date = "2018-01-22"
                stat = Statisque.objects.filter(date_heure__range=(start_date, end_date)).values('id', 'date_heure',
                                                                                                 'idUser',
                                                                                                 'idUser__nom',
                                                                                                 'idUser__prenom',
                                                                                                 'idUser__civilite',
                                                                                                 'idUser__dateNaiss')

                # stat01 = Statisque.objects.filter(date_heure__range=(start_date, end_date)).annotate(dcount=Count('date_heure')).dates('date_heure', 'day').annotate(c=Count('id'))

                abscisse = Statisque.objects.filter(date_heure__range=(start_date, end_date)).dates('date_heure', 'day')
                ordonnees = Statisque.objects.filter(date_heure__range=(start_date, end_date)).annotate(
                    c=Count('id')).dates('date_heure', 'day').annotate(c=Count('date_heure'))
                print(' abscisse ')
                print(' abscisse ')
                print(abscisse)
                print(abscisse)
                print(' ordonnees ')
                print(' ordonnees ')
                print(ordonnees)
                print(ordonnees)

                stat0001 = Statisque.objects.extra(
                    select={
                        'valeur': "SELECT *, COUNT(date_heure) FROM users_statisque GROUP BY date_heure"
                    }
                )

                stat02 = Statisque.objects.values('date_heure').annotate(dcount=Count('date_heure')).filter(
                    date_heure__range=(start_date, end_date))
                print(' stat02 ')
                print(' stat02 ')
                print(' stat02 ')
                print(stat02)
                print(stat02)

            elif int(request.POST['semaine']) == 4:
                start_date = "2018-01-22"
                end_date = "2018-01-29"
                stat = Statisque.objects.filter(date_heure__range=(start_date, end_date)).values('id', 'date_heure',
                                                                                                 'idUser',
                                                                                                 'idUser__nom',
                                                                                                 'idUser__prenom',
                                                                                                 'idUser__civilite',
                                                                                                 'idUser__dateNaiss')

                # stat01 = Statisque.objects.filter(date_heure__range=(start_date, end_date)).annotate(dcount=Count('date_heure')).dates('date_heure', 'day').annotate(c=Count('id'))

                abscisse = Statisque.objects.filter(date_heure__range=(start_date, end_date)).dates('date_heure', 'day')
                ordonnees = Statisque.objects.filter(date_heure__range=(start_date, end_date)).annotate(
                    c=Count('id')).dates('date_heure', 'day').annotate(c=Count('date_heure'))
                print(' abscisse ')
                print(' abscisse ')
                print(abscisse)
                print(abscisse)
                print(' ordonnees ')
                print(' ordonnees ')
                print(ordonnees)
                print(ordonnees)

                stat0001 = Statisque.objects.extra(
                    select={
                        'valeur': "SELECT *, COUNT(date_heure) FROM users_statisque GROUP BY date_heure"
                    }
                )

                stat02 = Statisque.objects.values('date_heure').annotate(dcount=Count('date_heure')).filter(
                    date_heure__range=(start_date, end_date))
                print(' stat02 ')
                print(' stat02 ')
                print(' stat02 ')
                print(stat02)
                print(stat02)

            elif int(request.POST['semaine']) == 5:
                start_date = "2018-01-29"
                end_date = "2018-02-05"
                stat = Statisque.objects.filter(date_heure__range=(start_date, end_date)).values('id', 'date_heure',
                                                                                                 'idUser',
                                                                                                 'idUser__nom',
                                                                                                 'idUser__prenom',
                                                                                                 'idUser__civilite',
                                                                                                 'idUser__dateNaiss')

                # stat01 = Statisque.objects.filter(date_heure__range=(start_date, end_date)).annotate(dcount=Count('date_heure')).dates('date_heure', 'day').annotate(c=Count('id'))

                abscisse = Statisque.objects.filter(date_heure__range=(start_date, end_date)).dates('date_heure', 'day')
                ordonnees = Statisque.objects.filter(date_heure__range=(start_date, end_date)).annotate(
                    c=Count('id')).dates('date_heure', 'day').annotate(c=Count('date_heure'))
                print(' abscisse ')
                print(' abscisse ')
                print(abscisse)
                print(abscisse)
                print(' ordonnees ')
                print(' ordonnees ')
                print(ordonnees)
                print(ordonnees)

                stat0001 = Statisque.objects.extra(
                    select={
                        'valeur': "SELECT *, COUNT(date_heure) FROM users_statisque GROUP BY date_heure"
                    }
                )

                stat02 = Statisque.objects.values('date_heure').annotate(dcount=Count('date_heure')).filter(
                    date_heure__range=(start_date, end_date))
                print(' stat02 ')
                print(' stat02 ')
                print(' stat02 ')
                print(stat02)
                print(stat02)

            elif int(request.POST['semaine']) == 6:
                start_date = "2018-02-05"
                end_date = "2018-02-12"
                stat = Statisque.objects.filter(date_heure__range=(start_date, end_date)).values('id', 'date_heure',
                                                                                                 'idUser',
                                                                                                 'idUser__nom',
                                                                                                 'idUser__prenom',
                                                                                                 'idUser__civilite',
                                                                                                 'idUser__dateNaiss')

                # stat01 = Statisque.objects.filter(date_heure__range=(start_date, end_date)).annotate(dcount=Count('date_heure')).dates('date_heure', 'day').annotate(c=Count('id'))

                abscisse = Statisque.objects.filter(date_heure__range=(start_date, end_date)).dates('date_heure', 'day')
                ordonnees = Statisque.objects.filter(date_heure__range=(start_date, end_date)).annotate(
                    c=Count('id')).dates('date_heure', 'day').annotate(c=Count('date_heure'))
                print(' abscisse ')
                print(' abscisse ')
                print(abscisse)
                print(abscisse)
                print(' ordonnees ')
                print(' ordonnees ')
                print(ordonnees)
                print(ordonnees)

                stat0001 = Statisque.objects.extra(
                    select={
                        'valeur': "SELECT *, COUNT(date_heure) FROM users_statisque GROUP BY date_heure"
                    }
                )

                stat02 = Statisque.objects.values('date_heure').annotate(dcount=Count('date_heure')).filter(
                    date_heure__range=(start_date, end_date))
                print(' stat02 ')
                print(' stat02 ')
                print(' stat02 ')
                print(stat02)
                print(stat02)

            elif int(request.POST['semaine']) == 7:
                start_date = "2018-02-12"
                end_date = "2018-02-19"
                stat = Statisque.objects.filter(date_heure__range=(start_date, end_date)).values('id', 'date_heure',
                                                                                                 'idUser',
                                                                                                 'idUser__nom',
                                                                                                 'idUser__prenom',
                                                                                                 'idUser__civilite',
                                                                                                 'idUser__dateNaiss')

                # stat01 = Statisque.objects.filter(date_heure__range=(start_date, end_date)).annotate(dcount=Count('date_heure')).dates('date_heure', 'day').annotate(c=Count('id'))

                abscisse = Statisque.objects.filter(date_heure__range=(start_date, end_date)).dates('date_heure', 'day')
                ordonnees = Statisque.objects.filter(date_heure__range=(start_date, end_date)).annotate(
                    c=Count('id')).dates('date_heure', 'day').annotate(c=Count('date_heure'))
                print(' abscisse ')
                print(' abscisse ')
                print(abscisse)
                print(abscisse)
                print(' ordonnees ')
                print(' ordonnees ')
                print(ordonnees)
                print(ordonnees)

                stat0001 = Statisque.objects.extra(
                    select={
                        'valeur': "SELECT *, COUNT(date_heure) FROM users_statisque GROUP BY date_heure"
                    }
                )

                stat02 = Statisque.objects.values('date_heure').annotate(dcount=Count('date_heure')).filter(
                    date_heure__range=(start_date, end_date))
                print(' stat02 ')
                print(' stat02 ')
                print(' stat02 ')
                print(stat02)
                print(stat02)
            elif int(request.POST['semaine']) == 8:
                start_date = "2018-02-19"
                end_date = "2018-02-26"
                stat = Statisque.objects.filter(date_heure__range=(start_date, end_date)).values('id', 'date_heure',
                                                                                                 'idUser',
                                                                                                 'idUser__nom',
                                                                                                 'idUser__prenom',
                                                                                                 'idUser__civilite',
                                                                                                 'idUser__dateNaiss')

                # stat01 = Statisque.objects.filter(date_heure__range=(start_date, end_date)).annotate(dcount=Count('date_heure')).dates('date_heure', 'day').annotate(c=Count('id'))

                abscisse = Statisque.objects.filter(date_heure__range=(start_date, end_date)).dates('date_heure', 'day')
                ordonnees = Statisque.objects.filter(date_heure__range=(start_date, end_date)).annotate(
                    c=Count('id')).dates('date_heure', 'day').annotate(c=Count('date_heure'))
                print(' abscisse ')
                print(' abscisse ')
                print(abscisse)
                print(abscisse)
                print(' ordonnees ')
                print(' ordonnees ')
                print(ordonnees)
                print(ordonnees)

                stat0001 = Statisque.objects.extra(
                    select={
                        'valeur': "SELECT *, COUNT(date_heure) FROM users_statisque GROUP BY date_heure"
                    }
                )

                stat02 = Statisque.objects.values('date_heure').annotate(dcount=Count('date_heure')).filter(
                    date_heure__range=(start_date, end_date))
                print(' stat02 ')
                print(' stat02 ')
                print(' stat02 ')
                print(stat02)
                print(stat02)

            elif int(request.POST['semaine']) == 9:
                start_date = "2018-02-26"
                end_date = "2018-03-05"
                stat = Statisque.objects.filter(date_heure__range=(start_date, end_date)).values('id', 'date_heure',
                                                                                                 'idUser',
                                                                                                 'idUser__nom',
                                                                                                 'idUser__prenom',
                                                                                                 'idUser__civilite',
                                                                                                 'idUser__dateNaiss')

                # stat01 = Statisque.objects.filter(date_heure__range=(start_date, end_date)).annotate(dcount=Count('date_heure')).dates('date_heure', 'day').annotate(c=Count('id'))

                abscisse = Statisque.objects.filter(date_heure__range=(start_date, end_date)).dates('date_heure', 'day')
                ordonnees = Statisque.objects.filter(date_heure__range=(start_date, end_date)).annotate(
                    c=Count('id')).dates('date_heure', 'day').annotate(c=Count('date_heure'))
                print(' abscisse ')
                print(' abscisse ')
                print(abscisse)
                print(abscisse)
                print(' ordonnees ')
                print(' ordonnees ')
                print(ordonnees)
                print(ordonnees)

                stat0001 = Statisque.objects.extra(
                    select={
                        'valeur': "SELECT *, COUNT(date_heure) FROM users_statisque GROUP BY date_heure"
                    }
                )

                stat02 = Statisque.objects.values('date_heure').annotate(dcount=Count('date_heure')).filter(
                    date_heure__range=(start_date, end_date))
                print(' stat02 ')
                print(' stat02 ')
                print(' stat02 ')
                print(stat02)
                print(stat02)


            elif int(request.POST['semaine']) == 10:
                start_date = "2018-03-05"
                end_date = "2018-03-12"
                stat = Statisque.objects.filter(date_heure__range=(start_date, end_date)).values('id', 'date_heure',
                                                                                                 'idUser',
                                                                                                 'idUser__nom',
                                                                                                 'idUser__prenom',
                                                                                                 'idUser__civilite',
                                                                                                 'idUser__dateNaiss')

                # stat01 = Statisque.objects.filter(date_heure__range=(start_date, end_date)).annotate(dcount=Count('date_heure')).dates('date_heure', 'day').annotate(c=Count('id'))

                abscisse = Statisque.objects.filter(date_heure__range=(start_date, end_date)).dates('date_heure', 'day')
                ordonnees = Statisque.objects.filter(date_heure__range=(start_date, end_date)).annotate(
                    c=Count('id')).dates('date_heure', 'day').annotate(c=Count('date_heure'))
                print(' abscisse ')
                print(' abscisse ')
                print(abscisse)
                print(abscisse)
                print(' ordonnees ')
                print(' ordonnees ')
                print(ordonnees)
                print(ordonnees)

                stat0001 = Statisque.objects.extra(
                    select={
                        'valeur': "SELECT *, COUNT(date_heure) FROM users_statisque GROUP BY date_heure"
                    }
                )

                stat02 = Statisque.objects.values('date_heure').annotate(dcount=Count('date_heure')).filter(
                    date_heure__range=(start_date, end_date))
                print(' stat02 ')
                print(' stat02 ')
                print(' stat02 ')
                print(stat02)
                print(stat02)

            elif int(request.POST['semaine']) == 11:
                start_date = "2018-03-12"
                end_date = "2018-03-19"
                stat = Statisque.objects.filter(date_heure__range=(start_date, end_date)).values('id', 'date_heure',
                                                                                                 'idUser',
                                                                                                 'idUser__nom',
                                                                                                 'idUser__prenom',
                                                                                                 'idUser__civilite',
                                                                                                 'idUser__dateNaiss')

                # stat01 = Statisque.objects.filter(date_heure__range=(start_date, end_date)).annotate(dcount=Count('date_heure')).dates('date_heure', 'day').annotate(c=Count('id'))

                abscisse = Statisque.objects.filter(date_heure__range=(start_date, end_date)).dates('date_heure', 'day')
                ordonnees = Statisque.objects.filter(date_heure__range=(start_date, end_date)).annotate(
                    c=Count('id')).dates('date_heure', 'day').annotate(c=Count('date_heure'))
                print(' abscisse ')
                print(' abscisse ')
                print(abscisse)
                print(abscisse)
                print(' ordonnees ')
                print(' ordonnees ')
                print(ordonnees)
                print(ordonnees)

                stat0001 = Statisque.objects.extra(
                    select={
                        'valeur': "SELECT *, COUNT(date_heure) FROM users_statisque GROUP BY date_heure"
                    }
                )

                stat02 = Statisque.objects.values('date_heure').annotate(dcount=Count('date_heure')).filter(
                    date_heure__range=(start_date, end_date))
                print(' stat02 ')
                print(' stat02 ')
                print(' stat02 ')
                print(stat02)
                print(stat02)

            elif int(request.POST['semaine']) == 12:
                start_date = "2018-03-19"
                end_date = "2018-03-26"
                stat = Statisque.objects.filter(date_heure__range=(start_date, end_date)).values('id', 'date_heure',
                                                                                                 'idUser',
                                                                                                 'idUser__nom',
                                                                                                 'idUser__prenom',
                                                                                                 'idUser__civilite',
                                                                                                 'idUser__dateNaiss')

                # stat01 = Statisque.objects.filter(date_heure__range=(start_date, end_date)).annotate(dcount=Count('date_heure')).dates('date_heure', 'day').annotate(c=Count('id'))

                abscisse = Statisque.objects.filter(date_heure__range=(start_date, end_date)).dates('date_heure', 'day')
                ordonnees = Statisque.objects.filter(date_heure__range=(start_date, end_date)).annotate(
                    c=Count('id')).dates('date_heure', 'day').annotate(c=Count('date_heure'))
                print(' abscisse ')
                print(' abscisse ')
                print(abscisse)
                print(abscisse)
                print(' ordonnees ')
                print(' ordonnees ')
                print(ordonnees)
                print(ordonnees)

                stat0001 = Statisque.objects.extra(
                    select={
                        'valeur': "SELECT *, COUNT(date_heure) FROM users_statisque GROUP BY date_heure"
                    }
                )

                stat02 = Statisque.objects.values('date_heure').annotate(dcount=Count('date_heure')).filter(
                    date_heure__range=(start_date, end_date))
                print(' stat02 ')
                print(' stat02 ')
                print(' stat02 ')
                print(stat02)
                print(stat02)

            elif int(request.POST['semaine']) == 13:
                start_date = "2018-03-26"
                end_date = "2018-04-02"
                stat = Statisque.objects.filter(date_heure__range=(start_date, end_date)).values('id', 'date_heure',
                                                                                                 'idUser',
                                                                                                 'idUser__nom',
                                                                                                 'idUser__prenom',
                                                                                                 'idUser__civilite',
                                                                                                 'idUser__dateNaiss')

                # stat01 = Statisque.objects.filter(date_heure__range=(start_date, end_date)).annotate(dcount=Count('date_heure')).dates('date_heure', 'day').annotate(c=Count('id'))

                abscisse = Statisque.objects.filter(date_heure__range=(start_date, end_date)).dates('date_heure', 'day')
                ordonnees = Statisque.objects.filter(date_heure__range=(start_date, end_date)).annotate(
                    c=Count('id')).dates('date_heure', 'day').annotate(c=Count('date_heure'))
                print(' abscisse ')
                print(' abscisse ')
                print(abscisse)
                print(abscisse)
                print(' ordonnees ')
                print(' ordonnees ')
                print(ordonnees)
                print(ordonnees)

                stat0001 = Statisque.objects.extra(
                    select={
                        'valeur': "SELECT *, COUNT(date_heure) FROM users_statisque GROUP BY date_heure"
                    }
                )

                stat02 = Statisque.objects.values('date_heure').annotate(dcount=Count('date_heure')).filter(
                    date_heure__range=(start_date, end_date))
                print(' stat02 ')
                print(' stat02 ')
                print(' stat02 ')
                print(stat02)
                print(stat02)

            elif int(request.POST['semaine']) == 14:
                start_date = "2018-04-02"
                end_date = "2018-04-09"
                stat = Statisque.objects.filter(date_heure__range=(start_date, end_date)).values('id', 'date_heure',
                                                                                                 'idUser',
                                                                                                 'idUser__nom',
                                                                                                 'idUser__prenom',
                                                                                                 'idUser__civilite',
                                                                                                 'idUser__dateNaiss')

                # stat01 = Statisque.objects.filter(date_heure__range=(start_date, end_date)).annotate(dcount=Count('date_heure')).dates('date_heure', 'day').annotate(c=Count('id'))

                abscisse = Statisque.objects.filter(date_heure__range=(start_date, end_date)).dates('date_heure', 'day')
                ordonnees = Statisque.objects.filter(date_heure__range=(start_date, end_date)).annotate(
                    c=Count('id')).dates('date_heure', 'day').annotate(c=Count('date_heure'))
                print(' abscisse ')
                print(' abscisse ')
                print(abscisse)
                print(abscisse)
                print(' ordonnees ')
                print(' ordonnees ')
                print(ordonnees)
                print(ordonnees)

                stat0001 = Statisque.objects.extra(
                    select={
                        'valeur': "SELECT *, COUNT(date_heure) FROM users_statisque GROUP BY date_heure"
                    }
                )

                stat02 = Statisque.objects.values('date_heure').annotate(dcount=Count('date_heure')).filter(
                    date_heure__range=(start_date, end_date))
                print(' stat02 ')
                print(' stat02 ')
                print(' stat02 ')
                print(stat02)
                print(stat02)

            elif int(request.POST['semaine']) == 15:
                start_date = "2018-04-09"
                end_date = "2018-04-16"
                stat = Statisque.objects.filter(date_heure__range=(start_date, end_date)).values('id', 'date_heure',
                                                                                                 'idUser',
                                                                                                 'idUser__nom',
                                                                                                 'idUser__prenom',
                                                                                                 'idUser__civilite',
                                                                                                 'idUser__dateNaiss')

                # stat01 = Statisque.objects.filter(date_heure__range=(start_date, end_date)).annotate(dcount=Count('date_heure')).dates('date_heure', 'day').annotate(c=Count('id'))

                abscisse = Statisque.objects.filter(date_heure__range=(start_date, end_date)).dates('date_heure', 'day')
                ordonnees = Statisque.objects.filter(date_heure__range=(start_date, end_date)).annotate(
                    c=Count('id')).dates('date_heure', 'day').annotate(c=Count('date_heure'))
                print(' abscisse ')
                print(' abscisse ')
                print(abscisse)
                print(abscisse)
                print(' ordonnees ')
                print(' ordonnees ')
                print(ordonnees)
                print(ordonnees)

                stat0001 = Statisque.objects.extra(
                    select={
                        'valeur': "SELECT *, COUNT(date_heure) FROM users_statisque GROUP BY date_heure"
                    }
                )

                stat02 = Statisque.objects.values('date_heure').annotate(dcount=Count('date_heure')).filter(
                    date_heure__range=(start_date, end_date))
                print(' stat02 ')
                print(' stat02 ')
                print(' stat02 ')
                print(stat02)
                print(stat02)

            elif int(request.POST['semaine']) == 16:
                start_date = "2018-04-16"
                end_date = "2018-04-23"
                stat = Statisque.objects.filter(date_heure__range=(start_date, end_date)).values('id', 'date_heure',
                                                                                                 'idUser',
                                                                                                 'idUser__nom',
                                                                                                 'idUser__prenom',
                                                                                                 'idUser__civilite',
                                                                                                 'idUser__dateNaiss')

                # stat01 = Statisque.objects.filter(date_heure__range=(start_date, end_date)).annotate(dcount=Count('date_heure')).dates('date_heure', 'day').annotate(c=Count('id'))

                abscisse = Statisque.objects.filter(date_heure__range=(start_date, end_date)).dates('date_heure', 'day')
                ordonnees = Statisque.objects.filter(date_heure__range=(start_date, end_date)).annotate(
                    c=Count('id')).dates('date_heure', 'day').annotate(c=Count('date_heure'))
                print(' abscisse ')
                print(' abscisse ')
                print(abscisse)
                print(abscisse)
                print(' ordonnees ')
                print(' ordonnees ')
                print(ordonnees)
                print(ordonnees)

                stat0001 = Statisque.objects.extra(
                    select={
                        'valeur': "SELECT *, COUNT(date_heure) FROM users_statisque GROUP BY date_heure"
                    }
                )

                stat02 = Statisque.objects.values('date_heure').annotate(dcount=Count('date_heure')).filter(
                    date_heure__range=(start_date, end_date))
                print(' stat02 ')
                print(' stat02 ')
                print(' stat02 ')
                print(stat02)
                print(stat02)

            elif int(request.POST['semaine']) == 17:
                start_date = "2018-04-23"
                end_date = "2018-04-30"
                stat = Statisque.objects.filter(date_heure__range=(start_date, end_date)).values('id', 'date_heure',
                                                                                                 'idUser',
                                                                                                 'idUser__nom',
                                                                                                 'idUser__prenom',
                                                                                                 'idUser__civilite',
                                                                                                 'idUser__dateNaiss')

                # stat01 = Statisque.objects.filter(date_heure__range=(start_date, end_date)).annotate(dcount=Count('date_heure')).dates('date_heure', 'day').annotate(c=Count('id'))

                abscisse = Statisque.objects.filter(date_heure__range=(start_date, end_date)).dates('date_heure', 'day')
                ordonnees = Statisque.objects.filter(date_heure__range=(start_date, end_date)).annotate(
                    c=Count('id')).dates('date_heure', 'day').annotate(c=Count('date_heure'))
                print(' abscisse ')
                print(' abscisse ')
                print(abscisse)
                print(abscisse)
                print(' ordonnees ')
                print(' ordonnees ')
                print(ordonnees)
                print(ordonnees)

                stat0001 = Statisque.objects.extra(
                    select={
                        'valeur': "SELECT *, COUNT(date_heure) FROM users_statisque GROUP BY date_heure"
                    }
                )

                stat02 = Statisque.objects.values('date_heure').annotate(dcount=Count('date_heure')).filter(
                    date_heure__range=(start_date, end_date))
                print(' stat02 ')
                print(' stat02 ')
                print(' stat02 ')
                print(stat02)
                print(stat02)
            elif int(request.POST['semaine']) == 18:
                start_date = "2018-04-30"
                end_date = "2018-05-07"
                stat = Statisque.objects.filter(date_heure__range=(start_date, end_date)).values('id', 'date_heure',
                                                                                                 'idUser',
                                                                                                 'idUser__nom',
                                                                                                 'idUser__prenom',
                                                                                                 'idUser__civilite',
                                                                                                 'idUser__dateNaiss')

                # stat01 = Statisque.objects.filter(date_heure__range=(start_date, end_date)).annotate(dcount=Count('date_heure')).dates('date_heure', 'day').annotate(c=Count('id'))

                abscisse = Statisque.objects.filter(date_heure__range=(start_date, end_date)).dates('date_heure', 'day')
                ordonnees = Statisque.objects.filter(date_heure__range=(start_date, end_date)).annotate(
                    c=Count('id')).dates('date_heure', 'day').annotate(c=Count('date_heure'))
                print(' abscisse ')
                print(' abscisse ')
                print(abscisse)
                print(abscisse)
                print(' ordonnees ')
                print(' ordonnees ')
                print(ordonnees)
                print(ordonnees)

                stat0001 = Statisque.objects.extra(
                    select={
                        'valeur': "SELECT *, COUNT(date_heure) FROM users_statisque GROUP BY date_heure"
                    }
                )

                stat02 = Statisque.objects.values('date_heure').annotate(dcount=Count('date_heure')).filter(
                    date_heure__range=(start_date, end_date))
                print(' stat02 ')
                print(' stat02 ')
                print(' stat02 ')
                print(stat02)
                print(stat02)

            elif int(request.POST['semaine'])==19:
                start_date = "2018-05-07"
                end_date = "2018-05-14"
                stat = Statisque.objects.filter(date_heure__range=(start_date, end_date)).values('id', 'date_heure',
                                                                                                 'idUser',
                                                                                                 'idUser__nom',
                                                                                                 'idUser__prenom',
                                                                                                 'idUser__civilite',
                                                                                                 'idUser__dateNaiss')

                # stat01 = Statisque.objects.filter(date_heure__range=(start_date, end_date)).annotate(dcount=Count('date_heure')).dates('date_heure', 'day').annotate(c=Count('id'))

                abscisse = Statisque.objects.filter(date_heure__range=(start_date, end_date)).dates('date_heure', 'day')
                ordonnees = Statisque.objects.filter(date_heure__range=(start_date, end_date)).annotate(
                    c=Count('id')).dates('date_heure', 'day').annotate(c=Count('date_heure'))
                print(' abscisse ')
                print(' abscisse ')
                print(abscisse)
                print(abscisse)
                print(' ordonnees ')
                print(' ordonnees ')
                print(ordonnees)
                print(ordonnees)

                stat0001 = Statisque.objects.extra(
                    select={
                        'valeur': "SELECT *, COUNT(date_heure) FROM users_statisque GROUP BY date_heure"
                    }
                )

                stat02 = Statisque.objects.values('date_heure').annotate(dcount=Count('date_heure')).filter(
                    date_heure__range=(start_date, end_date))
                print(' stat02 ')
                print(' stat02 ')
                print(' stat02 ')
                print(stat02)
                print(stat02)

            elif int(request.POST['semaine'])==20:
                start_date = "2018-05-14"
                end_date = "2018-05-21"
                stat = Statisque.objects.filter(date_heure__range=(start_date, end_date)).values('id', 'date_heure',
                                                                                                 'idUser',
                                                                                                 'idUser__nom',
                                                                                                 'idUser__prenom',
                                                                                                 'idUser__civilite',
                                                                                                 'idUser__dateNaiss')

                # stat01 = Statisque.objects.filter(date_heure__range=(start_date, end_date)).annotate(dcount=Count('date_heure')).dates('date_heure', 'day').annotate(c=Count('id'))

                abscisse = Statisque.objects.filter(date_heure__range=(start_date, end_date)).dates('date_heure', 'day')
                ordonnees = Statisque.objects.filter(date_heure__range=(start_date, end_date)).annotate(
                    c=Count('id')).dates('date_heure', 'day').annotate(c=Count('date_heure'))
                print(' abscisse ')
                print(' abscisse ')
                print(abscisse)
                print(abscisse)
                print(' ordonnees ')
                print(' ordonnees ')
                print(ordonnees)
                print(ordonnees)

                stat0001 = Statisque.objects.extra(
                    select={
                        'valeur': "SELECT *, COUNT(date_heure) FROM users_statisque GROUP BY date_heure"
                    }
                )

                stat02 = Statisque.objects.values('date_heure').annotate(dcount=Count('date_heure')).filter(
                    date_heure__range=(start_date, end_date))
                print(' stat02 ')
                print(' stat02 ')
                print(' stat02 ')
                print(stat02)
                print(stat02)

            elif int(request.POST['semaine'])==21:
                start_date = "2018-05-21"
                end_date = "2018-05-28"
                stat = Statisque.objects.filter(date_heure__range=(start_date, end_date)).values('id', 'date_heure',
                                                                                                 'idUser',
                                                                                                 'idUser__nom',
                                                                                                 'idUser__prenom',
                                                                                                 'idUser__civilite',
                                                                                                 'idUser__dateNaiss')

                # stat01 = Statisque.objects.filter(date_heure__range=(start_date, end_date)).annotate(dcount=Count('date_heure')).dates('date_heure', 'day').annotate(c=Count('id'))

                abscisse = Statisque.objects.filter(date_heure__range=(start_date, end_date)).dates('date_heure', 'day')
                ordonnees = Statisque.objects.filter(date_heure__range=(start_date, end_date)).annotate(
                    c=Count('id')).dates('date_heure', 'day').annotate(c=Count('date_heure'))
                print(' abscisse ')
                print(' abscisse ')
                print(abscisse)
                print(abscisse)
                print(' ordonnees ')
                print(' ordonnees ')
                print(ordonnees)
                print(ordonnees)

                stat0001 = Statisque.objects.extra(
                    select={
                        'valeur': "SELECT *, COUNT(date_heure) FROM users_statisque GROUP BY date_heure"
                    }
                )

                stat02 = Statisque.objects.values('date_heure').annotate(dcount=Count('date_heure')).filter(
                    date_heure__range=(start_date, end_date))
                print(' stat02 ')
                print(' stat02 ')
                print(' stat02 ')
                print(stat02)
                print(stat02)

            elif int(request.POST['semaine'])==22:
                start_date = "2018-05-28"
                end_date = "2018-06-04"
                stat = Statisque.objects.filter(date_heure__range=(start_date, end_date)).values('id', 'date_heure',
                                                                                                 'idUser',
                                                                                                 'idUser__nom',
                                                                                                 'idUser__prenom',
                                                                                                 'idUser__civilite',
                                                                                                 'idUser__dateNaiss')

                # stat01 = Statisque.objects.filter(date_heure__range=(start_date, end_date)).annotate(dcount=Count('date_heure')).dates('date_heure', 'day').annotate(c=Count('id'))

                abscisse = Statisque.objects.filter(date_heure__range=(start_date, end_date)).dates('date_heure', 'day')
                ordonnees = Statisque.objects.filter(date_heure__range=(start_date, end_date)).annotate(
                    c=Count('id')).dates('date_heure', 'day').annotate(c=Count('date_heure'))
                print(' abscisse ')
                print(' abscisse ')
                print(abscisse)
                print(abscisse)
                print(' ordonnees ')
                print(' ordonnees ')
                print(ordonnees)
                print(ordonnees)

                stat0001 = Statisque.objects.extra(
                    select={
                        'valeur': "SELECT *, COUNT(date_heure) FROM users_statisque GROUP BY date_heure"
                    }
                )

                stat02 = Statisque.objects.values('date_heure').annotate(dcount=Count('date_heure')).filter(
                    date_heure__range=(start_date, end_date))
                print(' stat02 ')
                print(' stat02 ')
                print(' stat02 ')
                print(stat02)
                print(stat02)

            elif int(request.POST['semaine'])==23:
                start_date = "2018-06-04"
                end_date = "2018-06-11"
                stat = Statisque.objects.filter(date_heure__range=(start_date, end_date)).values('id', 'date_heure',
                                                                                                 'idUser',
                                                                                                 'idUser__nom',
                                                                                                 'idUser__prenom',
                                                                                                 'idUser__civilite',
                                                                                                 'idUser__dateNaiss')

                # stat01 = Statisque.objects.filter(date_heure__range=(start_date, end_date)).annotate(dcount=Count('date_heure')).dates('date_heure', 'day').annotate(c=Count('id'))

                abscisse = Statisque.objects.filter(date_heure__range=(start_date, end_date)).dates('date_heure', 'day')
                ordonnees = Statisque.objects.filter(date_heure__range=(start_date, end_date)).annotate(
                    c=Count('id')).dates('date_heure', 'day').annotate(c=Count('date_heure'))
                print(' abscisse ')
                print(' abscisse ')
                print(abscisse)
                print(abscisse)
                print(' ordonnees ')
                print(' ordonnees ')
                print(ordonnees)
                print(ordonnees)

                stat0001 = Statisque.objects.extra(
                    select={
                        'valeur': "SELECT *, COUNT(date_heure) FROM users_statisque GROUP BY date_heure"
                    }
                )

                stat02 = Statisque.objects.values('date_heure').annotate(dcount=Count('date_heure')).filter(
                    date_heure__range=(start_date, end_date))
                print(' stat02 ')
                print(' stat02 ')
                print(' stat02 ')
                print(stat02)
                print(stat02)
            elif int(request.POST['semaine'])==24:


                start_date = "2018-06-11"
                end_date = "2018-06-18"
                print(start_date)
                print(end_date)
                stat = Statisque.objects.filter(date_heure__range=(start_date, end_date)).values('id', 'date_heure',
                                                                                                 'idUser',
                                                                                                 'idUser__nom',
                                                                                                 'idUser__prenom',
                                                                                                 'idUser__civilite',
                                                                                                 'idUser__dateNaiss')

                # stat01 = Statisque.objects.filter(date_heure__range=(start_date, end_date)).annotate(dcount=Count('date_heure')).dates('date_heure', 'day').annotate(c=Count('id'))

                abscisse = Statisque.objects.filter(date_heure__range=(start_date, end_date)).dates('date_heure', 'day')
                ordonnees = Statisque.objects.filter(date_heure__range=(start_date, end_date)).annotate(
                    c=Count('id')).dates('date_heure', 'day').annotate(c=Count('date_heure'))
                print(' abscisse ')
                print(' abscisse ')
                print(abscisse)
                print(abscisse)
                print(' ordonnees ')
                print(' ordonnees ')
                print(ordonnees)
                print(ordonnees)

                stat0001 = Statisque.objects.extra(
                    select={
                        'valeur': "SELECT *, COUNT(date_heure) FROM users_statisque GROUP BY date_heure"
                    }
                )

                stat02 = Statisque.objects.values('date_heure').annotate(dcount=Count('date_heure')).filter(
                    date_heure__range=(start_date, end_date))
                print(' stat02 ')
                print(' stat02 ')
                print(' stat02 ')
                print(stat02)
                print(stat02)

            elif int(request.POST['semaine']) == 25:
                start_date = "2018-06-18"
                end_date = "2018-06-25"
                stat = Statisque.objects.filter(date_heure__range=(start_date, end_date)).values('id', 'date_heure',
                                                                                                 'idUser',
                                                                                                 'idUser__nom',
                                                                                                 'idUser__prenom',
                                                                                                 'idUser__civilite',
                                                                                                 'idUser__dateNaiss')

                # stat01 = Statisque.objects.filter(date_heure__range=(start_date, end_date)).annotate(dcount=Count('date_heure')).dates('date_heure', 'day').annotate(c=Count('id'))

                abscisse = Statisque.objects.filter(date_heure__range=(start_date, end_date)).dates('date_heure', 'day')
                ordonnees = Statisque.objects.filter(date_heure__range=(start_date, end_date)).annotate(
                    c=Count('id')).dates('date_heure', 'day').annotate(c=Count('date_heure'))
                print(' abscisse ')
                print(' abscisse ')
                print(abscisse)
                print(abscisse)
                print(' ordonnees ')
                print(' ordonnees ')
                print(ordonnees)
                print(ordonnees)

                stat0001 = Statisque.objects.extra(
                    select={
                        'valeur': "SELECT *, COUNT(date_heure) FROM users_statisque GROUP BY date_heure"
                    }
                )

                stat02 = Statisque.objects.values('date_heure').annotate(dcount=Count('date_heure')).filter(
                    date_heure__range=(start_date, end_date))
                print(' stat02 ')
                print(' stat02 ')
                print(' stat02 ')
                print(stat02)
                print(stat02)

            elif int(request.POST['semaine']) == 26:
                start_date = "2018-06-25"
                end_date = "2018-07-02"
                stat = Statisque.objects.filter(date_heure__range=(start_date, end_date)).values('id', 'date_heure',
                                                                                                 'idUser',
                                                                                                 'idUser__nom',
                                                                                                 'idUser__prenom',
                                                                                                 'idUser__civilite',
                                                                                                 'idUser__dateNaiss')

                # stat01 = Statisque.objects.filter(date_heure__range=(start_date, end_date)).annotate(dcount=Count('date_heure')).dates('date_heure', 'day').annotate(c=Count('id'))

                abscisse = Statisque.objects.filter(date_heure__range=(start_date, end_date)).dates('date_heure', 'day')
                ordonnees = Statisque.objects.filter(date_heure__range=(start_date, end_date)).annotate(
                    c=Count('id')).dates('date_heure', 'day').annotate(c=Count('date_heure'))
                print(' abscisse ')
                print(' abscisse ')
                print(abscisse)
                print(abscisse)
                print(' ordonnees ')
                print(' ordonnees ')
                print(ordonnees)
                print(ordonnees)

                stat0001 = Statisque.objects.extra(
                    select={
                        'valeur': "SELECT *, COUNT(date_heure) FROM users_statisque GROUP BY date_heure"
                    }
                )

                stat02 = Statisque.objects.values('date_heure').annotate(dcount=Count('date_heure')).filter(
                    date_heure__range=(start_date, end_date))
                print(' stat02 ')
                print(' stat02 ')
                print(' stat02 ')
                print(stat02)
                print(stat02)

            elif int(request.POST['semaine']) == 27:
                start_date = "2018-07-02"
                end_date = "2018-07-09"
                stat = Statisque.objects.filter(date_heure__range=(start_date, end_date)).values('id', 'date_heure',
                                                                                                 'idUser',
                                                                                                 'idUser__nom',
                                                                                                 'idUser__prenom',
                                                                                                 'idUser__civilite',
                                                                                                 'idUser__dateNaiss')

                # stat01 = Statisque.objects.filter(date_heure__range=(start_date, end_date)).annotate(dcount=Count('date_heure')).dates('date_heure', 'day').annotate(c=Count('id'))

                abscisse = Statisque.objects.filter(date_heure__range=(start_date, end_date)).dates('date_heure', 'day')
                ordonnees = Statisque.objects.filter(date_heure__range=(start_date, end_date)).annotate(
                    c=Count('id')).dates('date_heure', 'day').annotate(c=Count('date_heure'))
                print(' abscisse ')
                print(' abscisse ')
                print(abscisse)
                print(abscisse)
                print(' ordonnees ')
                print(' ordonnees ')
                print(ordonnees)
                print(ordonnees)

                stat0001 = Statisque.objects.extra(
                    select={
                        'valeur': "SELECT *, COUNT(date_heure) FROM users_statisque GROUP BY date_heure"
                    }
                )

                stat02 = Statisque.objects.values('date_heure').annotate(dcount=Count('date_heure')).filter(
                    date_heure__range=(start_date, end_date))
                print(' stat02 ')
                print(' stat02 ')
                print(' stat02 ')
                print(stat02)
                print(stat02)

            elif int(request.POST['semaine']) == 28:
                start_date = "2018-07-09"
                end_date = "2018-07-16"
                stat = Statisque.objects.filter(date_heure__range=(start_date, end_date)).values('id', 'date_heure',
                                                                                                 'idUser',
                                                                                                 'idUser__nom',
                                                                                                 'idUser__prenom',
                                                                                                 'idUser__civilite',
                                                                                                 'idUser__dateNaiss')

                # stat01 = Statisque.objects.filter(date_heure__range=(start_date, end_date)).annotate(dcount=Count('date_heure')).dates('date_heure', 'day').annotate(c=Count('id'))

                abscisse = Statisque.objects.filter(date_heure__range=(start_date, end_date)).dates('date_heure', 'day')
                ordonnees = Statisque.objects.filter(date_heure__range=(start_date, end_date)).annotate(
                    c=Count('id')).dates('date_heure', 'day').annotate(c=Count('date_heure'))
                print(' abscisse ')
                print(' abscisse ')
                print(abscisse)
                print(abscisse)
                print(' ordonnees ')
                print(' ordonnees ')
                print(ordonnees)
                print(ordonnees)

                stat0001 = Statisque.objects.extra(
                    select={
                        'valeur': "SELECT *, COUNT(date_heure) FROM users_statisque GROUP BY date_heure"
                    }
                )

                stat02 = Statisque.objects.values('date_heure').annotate(dcount=Count('date_heure')).filter(
                    date_heure__range=(start_date, end_date))
                print(' stat02 ')
                print(' stat02 ')
                print(' stat02 ')
                print(stat02)
                print(stat02)

            elif int(request.POST['semaine']) == 29:
                start_date = "2018-07-16"
                end_date = "2018-07-23"
                stat = Statisque.objects.filter(date_heure__range=(start_date, end_date)).values('id', 'date_heure',
                                                                                                 'idUser',
                                                                                                 'idUser__nom',
                                                                                                 'idUser__prenom',
                                                                                                 'idUser__civilite',
                                                                                                 'idUser__dateNaiss')

                # stat01 = Statisque.objects.filter(date_heure__range=(start_date, end_date)).annotate(dcount=Count('date_heure')).dates('date_heure', 'day').annotate(c=Count('id'))

                abscisse = Statisque.objects.filter(date_heure__range=(start_date, end_date)).dates('date_heure', 'day')
                ordonnees = Statisque.objects.filter(date_heure__range=(start_date, end_date)).annotate(
                    c=Count('id')).dates('date_heure', 'day').annotate(c=Count('date_heure'))
                print(' abscisse ')
                print(' abscisse ')
                print(abscisse)
                print(abscisse)
                print(' ordonnees ')
                print(' ordonnees ')
                print(ordonnees)
                print(ordonnees)

                stat0001 = Statisque.objects.extra(
                    select={
                        'valeur': "SELECT *, COUNT(date_heure) FROM users_statisque GROUP BY date_heure"
                    }
                )

                stat02 = Statisque.objects.values('date_heure').annotate(dcount=Count('date_heure')).filter(
                    date_heure__range=(start_date, end_date))
                print(' stat02 ')
                print(' stat02 ')
                print(' stat02 ')
                print(stat02)
                print(stat02)

            elif int(request.POST['semaine']) == 30:
                start_date = "2018-07-23"
                end_date = "2018-07-30"
                stat = Statisque.objects.filter(date_heure__range=(start_date, end_date)).values('id', 'date_heure',
                                                                                                 'idUser',
                                                                                                 'idUser__nom',
                                                                                                 'idUser__prenom',
                                                                                                 'idUser__civilite',
                                                                                                 'idUser__dateNaiss')

                # stat01 = Statisque.objects.filter(date_heure__range=(start_date, end_date)).annotate(dcount=Count('date_heure')).dates('date_heure', 'day').annotate(c=Count('id'))

                abscisse = Statisque.objects.filter(date_heure__range=(start_date, end_date)).dates('date_heure', 'day')
                ordonnees = Statisque.objects.filter(date_heure__range=(start_date, end_date)).annotate(
                    c=Count('id')).dates('date_heure', 'day').annotate(c=Count('date_heure'))
                print(' abscisse ')
                print(' abscisse ')
                print(abscisse)
                print(abscisse)
                print(' ordonnees ')
                print(' ordonnees ')
                print(ordonnees)
                print(ordonnees)

                stat0001 = Statisque.objects.extra(
                    select={
                        'valeur': "SELECT *, COUNT(date_heure) FROM users_statisque GROUP BY date_heure"
                    }
                )

                stat02 = Statisque.objects.values('date_heure').annotate(dcount=Count('date_heure')).filter(
                    date_heure__range=(start_date, end_date))
                print(' stat02 ')
                print(' stat02 ')
                print(' stat02 ')
                print(stat02)
                print(stat02)

            elif int(request.POST['semaine']) == 31:
                start_date = "2018-07-30"
                end_date = "2018-08-06"
                stat = Statisque.objects.filter(date_heure__range=(start_date, end_date)).values('id', 'date_heure',
                                                                                                 'idUser',
                                                                                                 'idUser__nom',
                                                                                                 'idUser__prenom',
                                                                                                 'idUser__civilite',
                                                                                                 'idUser__dateNaiss')

                # stat01 = Statisque.objects.filter(date_heure__range=(start_date, end_date)).annotate(dcount=Count('date_heure')).dates('date_heure', 'day').annotate(c=Count('id'))

                abscisse = Statisque.objects.filter(date_heure__range=(start_date, end_date)).dates('date_heure', 'day')
                ordonnees = Statisque.objects.filter(date_heure__range=(start_date, end_date)).annotate(
                    c=Count('id')).dates('date_heure', 'day').annotate(c=Count('date_heure'))
                print(' abscisse ')
                print(' abscisse ')
                print(abscisse)
                print(abscisse)
                print(' ordonnees ')
                print(' ordonnees ')
                print(ordonnees)
                print(ordonnees)

                stat0001 = Statisque.objects.extra(
                    select={
                        'valeur': "SELECT *, COUNT(date_heure) FROM users_statisque GROUP BY date_heure"
                    }
                )

                stat02 = Statisque.objects.values('date_heure').annotate(dcount=Count('date_heure')).filter(
                    date_heure__range=(start_date, end_date))
                print(' stat02 ')
                print(' stat02 ')
                print(' stat02 ')
                print(stat02)
                print(stat02)

            elif int(request.POST['semaine']) == 32:
                start_date = "2018-08-06"
                end_date = "2018-08-13"
                stat = Statisque.objects.filter(date_heure__range=(start_date, end_date)).values('id', 'date_heure',
                                                                                                 'idUser',
                                                                                                 'idUser__nom',
                                                                                                 'idUser__prenom',
                                                                                                 'idUser__civilite',
                                                                                                 'idUser__dateNaiss')

                # stat01 = Statisque.objects.filter(date_heure__range=(start_date, end_date)).annotate(dcount=Count('date_heure')).dates('date_heure', 'day').annotate(c=Count('id'))

                abscisse = Statisque.objects.filter(date_heure__range=(start_date, end_date)).dates('date_heure', 'day')
                ordonnees = Statisque.objects.filter(date_heure__range=(start_date, end_date)).annotate(
                    c=Count('id')).dates('date_heure', 'day').annotate(c=Count('date_heure'))
                print(' abscisse ')
                print(' abscisse ')
                print(abscisse)
                print(abscisse)
                print(' ordonnees ')
                print(' ordonnees ')
                print(ordonnees)
                print(ordonnees)

                stat0001 = Statisque.objects.extra(
                    select={
                        'valeur': "SELECT *, COUNT(date_heure) FROM users_statisque GROUP BY date_heure"
                    }
                )

                stat02 = Statisque.objects.values('date_heure').annotate(dcount=Count('date_heure')).filter(
                    date_heure__range=(start_date, end_date))
                print(' stat02 ')
                print(' stat02 ')
                print(' stat02 ')
                print(stat02)
                print(stat02)

            elif int(request.POST['semaine']) == 33:
                start_date = "2018-08-13"
                end_date = "2018-08-20"
                stat = Statisque.objects.filter(date_heure__range=(start_date, end_date)).values('id', 'date_heure',
                                                                                                 'idUser',
                                                                                                 'idUser__nom',
                                                                                                 'idUser__prenom',
                                                                                                 'idUser__civilite',
                                                                                                 'idUser__dateNaiss')

                # stat01 = Statisque.objects.filter(date_heure__range=(start_date, end_date)).annotate(dcount=Count('date_heure')).dates('date_heure', 'day').annotate(c=Count('id'))

                abscisse = Statisque.objects.filter(date_heure__range=(start_date, end_date)).dates('date_heure', 'day')
                ordonnees = Statisque.objects.filter(date_heure__range=(start_date, end_date)).annotate(
                    c=Count('id')).dates('date_heure', 'day').annotate(c=Count('date_heure'))
                print(' abscisse ')
                print(' abscisse ')
                print(abscisse)
                print(abscisse)
                print(' ordonnees ')
                print(' ordonnees ')
                print(ordonnees)
                print(ordonnees)

                stat0001 = Statisque.objects.extra(
                    select={
                        'valeur': "SELECT *, COUNT(date_heure) FROM users_statisque GROUP BY date_heure"
                    }
                )

                stat02 = Statisque.objects.values('date_heure').annotate(dcount=Count('date_heure')).filter(
                    date_heure__range=(start_date, end_date))
                print(' stat02 ')
                print(' stat02 ')
                print(' stat02 ')
                print(stat02)
                print(stat02)
            elif int(request.POST['semaine']) == 34:
                start_date = "2018-08-20"
                end_date = "2018-08-27"
                stat = Statisque.objects.filter(date_heure__range=(start_date, end_date)).values('id', 'date_heure',
                                                                                                 'idUser',
                                                                                                 'idUser__nom',
                                                                                                 'idUser__prenom',
                                                                                                 'idUser__civilite',
                                                                                                 'idUser__dateNaiss')

                # stat01 = Statisque.objects.filter(date_heure__range=(start_date, end_date)).annotate(dcount=Count('date_heure')).dates('date_heure', 'day').annotate(c=Count('id'))

                abscisse = Statisque.objects.filter(date_heure__range=(start_date, end_date)).dates('date_heure', 'day')
                ordonnees = Statisque.objects.filter(date_heure__range=(start_date, end_date)).annotate(
                    c=Count('id')).dates('date_heure', 'day').annotate(c=Count('date_heure'))
                print(' abscisse ')
                print(' abscisse ')
                print(abscisse)
                print(abscisse)
                print(' ordonnees ')
                print(' ordonnees ')
                print(ordonnees)
                print(ordonnees)

                stat0001 = Statisque.objects.extra(
                    select={
                        'valeur': "SELECT *, COUNT(date_heure) FROM users_statisque GROUP BY date_heure"
                    }
                )

                stat02 = Statisque.objects.values('date_heure').annotate(dcount=Count('date_heure')).filter(
                    date_heure__range=(start_date, end_date))
                print(' stat02 ')
                print(' stat02 ')
                print(' stat02 ')
                print(stat02)
                print(stat02)

            elif int(request.POST['semaine']) == 35:
                start_date = "2018-08-27"
                end_date = "2018-09-03"
                stat = Statisque.objects.filter(date_heure__range=(start_date, end_date)).values('id', 'date_heure',
                                                                                                 'idUser',
                                                                                                 'idUser__nom',
                                                                                                 'idUser__prenom',
                                                                                                 'idUser__civilite',
                                                                                                 'idUser__dateNaiss')

                # stat01 = Statisque.objects.filter(date_heure__range=(start_date, end_date)).annotate(dcount=Count('date_heure')).dates('date_heure', 'day').annotate(c=Count('id'))

                abscisse = Statisque.objects.filter(date_heure__range=(start_date, end_date)).dates('date_heure', 'day')
                ordonnees = Statisque.objects.filter(date_heure__range=(start_date, end_date)).annotate(
                    c=Count('id')).dates('date_heure', 'day').annotate(c=Count('date_heure'))
                print(' abscisse ')
                print(' abscisse ')
                print(abscisse)
                print(abscisse)
                print(' ordonnees ')
                print(' ordonnees ')
                print(ordonnees)
                print(ordonnees)

                stat0001 = Statisque.objects.extra(
                    select={
                        'valeur': "SELECT *, COUNT(date_heure) FROM users_statisque GROUP BY date_heure"
                    }
                )

                stat02 = Statisque.objects.values('date_heure').annotate(dcount=Count('date_heure')).filter(
                    date_heure__range=(start_date, end_date))
                print(' stat02 ')
                print(' stat02 ')
                print(' stat02 ')
                print(stat02)
                print(stat02)
            elif int(request.POST['semaine']) == 36:
                start_date = "2018-09-03"
                end_date = "2018-09-10"
                stat = Statisque.objects.filter(date_heure__range=(start_date, end_date)).values('id', 'date_heure',
                                                                                                 'idUser',
                                                                                                 'idUser__nom',
                                                                                                 'idUser__prenom',
                                                                                                 'idUser__civilite',
                                                                                                 'idUser__dateNaiss')

                # stat01 = Statisque.objects.filter(date_heure__range=(start_date, end_date)).annotate(dcount=Count('date_heure')).dates('date_heure', 'day').annotate(c=Count('id'))

                abscisse = Statisque.objects.filter(date_heure__range=(start_date, end_date)).dates('date_heure', 'day')
                ordonnees = Statisque.objects.filter(date_heure__range=(start_date, end_date)).annotate(
                    c=Count('id')).dates('date_heure', 'day').annotate(c=Count('date_heure'))
                print(' abscisse ')
                print(' abscisse ')
                print(abscisse)
                print(abscisse)
                print(' ordonnees ')
                print(' ordonnees ')
                print(ordonnees)
                print(ordonnees)

                stat0001 = Statisque.objects.extra(
                    select={
                        'valeur': "SELECT *, COUNT(date_heure) FROM users_statisque GROUP BY date_heure"
                    }
                )

                stat02 = Statisque.objects.values('date_heure').annotate(dcount=Count('date_heure')).filter(
                    date_heure__range=(start_date, end_date))
                print(' stat02 ')
                print(' stat02 ')
                print(' stat02 ')
                print(stat02)
                print(stat02)

            elif int(request.POST['semaine']) == 37:
                start_date = "2018-09-10"
                end_date = "2018-09-17"
                stat = Statisque.objects.filter(date_heure__range=(start_date, end_date)).values('id', 'date_heure',
                                                                                                 'idUser',
                                                                                                 'idUser__nom',
                                                                                                 'idUser__prenom',
                                                                                                 'idUser__civilite',
                                                                                                 'idUser__dateNaiss')

                # stat01 = Statisque.objects.filter(date_heure__range=(start_date, end_date)).annotate(dcount=Count('date_heure')).dates('date_heure', 'day').annotate(c=Count('id'))

                abscisse = Statisque.objects.filter(date_heure__range=(start_date, end_date)).dates('date_heure', 'day')
                ordonnees = Statisque.objects.filter(date_heure__range=(start_date, end_date)).annotate(
                    c=Count('id')).dates('date_heure', 'day').annotate(c=Count('date_heure'))
                print(' abscisse ')
                print(' abscisse ')
                print(abscisse)
                print(abscisse)
                print(' ordonnees ')
                print(' ordonnees ')
                print(ordonnees)
                print(ordonnees)

                stat0001 = Statisque.objects.extra(
                    select={
                        'valeur': "SELECT *, COUNT(date_heure) FROM users_statisque GROUP BY date_heure"
                    }
                )

                stat02 = Statisque.objects.values('date_heure').annotate(dcount=Count('date_heure')).filter(
                    date_heure__range=(start_date, end_date))
                print(' stat02 ')
                print(' stat02 ')
                print(' stat02 ')
                print(stat02)
                print(stat02)

            elif int(request.POST['semaine']) == 38:
                start_date = "2018-09-17"
                end_date = "2018-09-24"
                stat = Statisque.objects.filter(date_heure__range=(start_date, end_date)).values('id', 'date_heure',
                                                                                                 'idUser',
                                                                                                 'idUser__nom',
                                                                                                 'idUser__prenom',
                                                                                                 'idUser__civilite',
                                                                                                 'idUser__dateNaiss')

                # stat01 = Statisque.objects.filter(date_heure__range=(start_date, end_date)).annotate(dcount=Count('date_heure')).dates('date_heure', 'day').annotate(c=Count('id'))

                abscisse = Statisque.objects.filter(date_heure__range=(start_date, end_date)).dates('date_heure', 'day')
                ordonnees = Statisque.objects.filter(date_heure__range=(start_date, end_date)).annotate(
                    c=Count('id')).dates('date_heure', 'day').annotate(c=Count('date_heure'))
                print(' abscisse ')
                print(' abscisse ')
                print(abscisse)
                print(abscisse)
                print(' ordonnees ')
                print(' ordonnees ')
                print(ordonnees)
                print(ordonnees)

                stat0001 = Statisque.objects.extra(
                    select={
                        'valeur': "SELECT *, COUNT(date_heure) FROM users_statisque GROUP BY date_heure"
                    }
                )

                stat02 = Statisque.objects.values('date_heure').annotate(dcount=Count('date_heure')).filter(
                    date_heure__range=(start_date, end_date))
                print(' stat02 ')
                print(' stat02 ')
                print(' stat02 ')
                print(stat02)
                print(stat02)

            elif int(request.POST['semaine']) == 39:
                start_date = "2018-09-24"
                end_date = "2018-10-01"
                stat = Statisque.objects.filter(date_heure__range=(start_date, end_date)).values('id', 'date_heure',
                                                                                                 'idUser',
                                                                                                 'idUser__nom',
                                                                                                 'idUser__prenom',
                                                                                                 'idUser__civilite',
                                                                                                 'idUser__dateNaiss')

                # stat01 = Statisque.objects.filter(date_heure__range=(start_date, end_date)).annotate(dcount=Count('date_heure')).dates('date_heure', 'day').annotate(c=Count('id'))

                abscisse = Statisque.objects.filter(date_heure__range=(start_date, end_date)).dates('date_heure', 'day')
                ordonnees = Statisque.objects.filter(date_heure__range=(start_date, end_date)).annotate(
                    c=Count('id')).dates('date_heure', 'day').annotate(c=Count('date_heure'))
                print(' abscisse ')
                print(' abscisse ')
                print(abscisse)
                print(abscisse)
                print(' ordonnees ')
                print(' ordonnees ')
                print(ordonnees)
                print(ordonnees)

                stat0001 = Statisque.objects.extra(
                    select={
                        'valeur': "SELECT *, COUNT(date_heure) FROM users_statisque GROUP BY date_heure"
                    }
                )

                stat02 = Statisque.objects.values('date_heure').annotate(dcount=Count('date_heure')).filter(
                    date_heure__range=(start_date, end_date))
                print(' stat02 ')
                print(' stat02 ')
                print(' stat02 ')
                print(stat02)
                print(stat02)
            elif int(request.POST['semaine']) == 40:
                start_date = "2018-10-01"
                end_date = "2018-10-08"
                stat = Statisque.objects.filter(date_heure__range=(start_date, end_date)).values('id', 'date_heure',
                                                                                                 'idUser',
                                                                                                 'idUser__nom',
                                                                                                 'idUser__prenom',
                                                                                                 'idUser__civilite',
                                                                                                 'idUser__dateNaiss')

                # stat01 = Statisque.objects.filter(date_heure__range=(start_date, end_date)).annotate(dcount=Count('date_heure')).dates('date_heure', 'day').annotate(c=Count('id'))

                abscisse = Statisque.objects.filter(date_heure__range=(start_date, end_date)).dates('date_heure', 'day')
                ordonnees = Statisque.objects.filter(date_heure__range=(start_date, end_date)).annotate(
                    c=Count('id')).dates('date_heure', 'day').annotate(c=Count('date_heure'))
                print(' abscisse ')
                print(' abscisse ')
                print(abscisse)
                print(abscisse)
                print(' ordonnees ')
                print(' ordonnees ')
                print(ordonnees)
                print(ordonnees)

                stat0001 = Statisque.objects.extra(
                    select={
                        'valeur': "SELECT *, COUNT(date_heure) FROM users_statisque GROUP BY date_heure"
                    }
                )

                stat02 = Statisque.objects.values('date_heure').annotate(dcount=Count('date_heure')).filter(
                    date_heure__range=(start_date, end_date))
                print(' stat02 ')
                print(' stat02 ')
                print(' stat02 ')
                print(stat02)
                print(stat02)

            elif int(request.POST['semaine']) == 41:
                start_date = "2018-10-08"
                end_date = "2018-10-15"
                stat = Statisque.objects.filter(date_heure__range=(start_date, end_date)).values('id', 'date_heure',
                                                                                                 'idUser',
                                                                                                 'idUser__nom',
                                                                                                 'idUser__prenom',
                                                                                                 'idUser__civilite',
                                                                                                 'idUser__dateNaiss')

                # stat01 = Statisque.objects.filter(date_heure__range=(start_date, end_date)).annotate(dcount=Count('date_heure')).dates('date_heure', 'day').annotate(c=Count('id'))

                abscisse = Statisque.objects.filter(date_heure__range=(start_date, end_date)).dates('date_heure', 'day')
                ordonnees = Statisque.objects.filter(date_heure__range=(start_date, end_date)).annotate(
                    c=Count('id')).dates('date_heure', 'day').annotate(c=Count('date_heure'))
                print(' abscisse ')
                print(' abscisse ')
                print(abscisse)
                print(abscisse)
                print(' ordonnees ')
                print(' ordonnees ')
                print(ordonnees)
                print(ordonnees)

                stat0001 = Statisque.objects.extra(
                    select={
                        'valeur': "SELECT *, COUNT(date_heure) FROM users_statisque GROUP BY date_heure"
                    }
                )

                stat02 = Statisque.objects.values('date_heure').annotate(dcount=Count('date_heure')).filter(
                    date_heure__range=(start_date, end_date))
                print(' stat02 ')
                print(' stat02 ')
                print(' stat02 ')
                print(stat02)
                print(stat02)

            elif int(request.POST['semaine']) == 42:
                start_date = "2018-10-15"
                end_date = "2018-10-22"
                stat = Statisque.objects.filter(date_heure__range=(start_date, end_date)).values('id', 'date_heure',
                                                                                                 'idUser',
                                                                                                 'idUser__nom',
                                                                                                 'idUser__prenom',
                                                                                                 'idUser__civilite',
                                                                                                 'idUser__dateNaiss')

                # stat01 = Statisque.objects.filter(date_heure__range=(start_date, end_date)).annotate(dcount=Count('date_heure')).dates('date_heure', 'day').annotate(c=Count('id'))

                abscisse = Statisque.objects.filter(date_heure__range=(start_date, end_date)).dates('date_heure', 'day')
                ordonnees = Statisque.objects.filter(date_heure__range=(start_date, end_date)).annotate(
                    c=Count('id')).dates('date_heure', 'day').annotate(c=Count('date_heure'))
                print(' abscisse ')
                print(' abscisse ')
                print(abscisse)
                print(abscisse)
                print(' ordonnees ')
                print(' ordonnees ')
                print(ordonnees)
                print(ordonnees)

                stat0001 = Statisque.objects.extra(
                    select={
                        'valeur': "SELECT *, COUNT(date_heure) FROM users_statisque GROUP BY date_heure"
                    }
                )

                stat02 = Statisque.objects.values('date_heure').annotate(dcount=Count('date_heure')).filter(
                    date_heure__range=(start_date, end_date))
                print(' stat02 ')
                print(' stat02 ')
                print(' stat02 ')
                print(stat02)
                print(stat02)

            elif int(request.POST['semaine']) == 43:
                start_date = "2018-10-22"
                end_date = "2018-10-29"
                stat = Statisque.objects.filter(date_heure__range=(start_date, end_date)).values('id', 'date_heure',
                                                                                                 'idUser',
                                                                                                 'idUser__nom',
                                                                                                 'idUser__prenom',
                                                                                                 'idUser__civilite',
                                                                                                 'idUser__dateNaiss')

                # stat01 = Statisque.objects.filter(date_heure__range=(start_date, end_date)).annotate(dcount=Count('date_heure')).dates('date_heure', 'day').annotate(c=Count('id'))

                abscisse = Statisque.objects.filter(date_heure__range=(start_date, end_date)).dates('date_heure', 'day')
                ordonnees = Statisque.objects.filter(date_heure__range=(start_date, end_date)).annotate(
                    c=Count('id')).dates('date_heure', 'day').annotate(c=Count('date_heure'))
                print(' abscisse ')
                print(' abscisse ')
                print(abscisse)
                print(abscisse)
                print(' ordonnees ')
                print(' ordonnees ')
                print(ordonnees)
                print(ordonnees)

                stat0001 = Statisque.objects.extra(
                    select={
                        'valeur': "SELECT *, COUNT(date_heure) FROM users_statisque GROUP BY date_heure"
                    }
                )

                stat02 = Statisque.objects.values('date_heure').annotate(dcount=Count('date_heure')).filter(
                    date_heure__range=(start_date, end_date))
                print(' stat02 ')
                print(' stat02 ')
                print(' stat02 ')
                print(stat02)
                print(stat02)
            elif int(request.POST['semaine']) == 44:
                start_date = "2018-10-29"
                end_date = "2018-11-05"
                stat = Statisque.objects.filter(date_heure__range=(start_date, end_date)).values('id', 'date_heure',
                                                                                                 'idUser',
                                                                                                 'idUser__nom',
                                                                                                 'idUser__prenom',
                                                                                                 'idUser__civilite',
                                                                                                 'idUser__dateNaiss')

                # stat01 = Statisque.objects.filter(date_heure__range=(start_date, end_date)).annotate(dcount=Count('date_heure')).dates('date_heure', 'day').annotate(c=Count('id'))

                abscisse = Statisque.objects.filter(date_heure__range=(start_date, end_date)).dates('date_heure', 'day')
                ordonnees = Statisque.objects.filter(date_heure__range=(start_date, end_date)).annotate(
                    c=Count('id')).dates('date_heure', 'day').annotate(c=Count('date_heure'))
                print(' abscisse ')
                print(' abscisse ')
                print(abscisse)
                print(abscisse)
                print(' ordonnees ')
                print(' ordonnees ')
                print(ordonnees)
                print(ordonnees)

                stat0001 = Statisque.objects.extra(
                    select={
                        'valeur': "SELECT *, COUNT(date_heure) FROM users_statisque GROUP BY date_heure"
                    }
                )

                stat02 = Statisque.objects.values('date_heure').annotate(dcount=Count('date_heure')).filter(
                    date_heure__range=(start_date, end_date))
                print(' stat02 ')
                print(' stat02 ')
                print(' stat02 ')
                print(stat02)
                print(stat02)

            elif int(request.POST['semaine']) == 45:
                start_date = "2018-11-05"
                end_date = "2018-11-12"
                stat = Statisque.objects.filter(date_heure__range=(start_date, end_date)).values('id', 'date_heure',
                                                                                                 'idUser',
                                                                                                 'idUser__nom',
                                                                                                 'idUser__prenom',
                                                                                                 'idUser__civilite',
                                                                                                 'idUser__dateNaiss')

                # stat01 = Statisque.objects.filter(date_heure__range=(start_date, end_date)).annotate(dcount=Count('date_heure')).dates('date_heure', 'day').annotate(c=Count('id'))

                abscisse = Statisque.objects.filter(date_heure__range=(start_date, end_date)).dates('date_heure', 'day')
                ordonnees = Statisque.objects.filter(date_heure__range=(start_date, end_date)).annotate(
                    c=Count('id')).dates('date_heure', 'day').annotate(c=Count('date_heure'))
                print(' abscisse ')
                print(' abscisse ')
                print(abscisse)
                print(abscisse)
                print(' ordonnees ')
                print(' ordonnees ')
                print(ordonnees)
                print(ordonnees)

                stat0001 = Statisque.objects.extra(
                    select={
                        'valeur': "SELECT *, COUNT(date_heure) FROM users_statisque GROUP BY date_heure"
                    }
                )

                stat02 = Statisque.objects.values('date_heure').annotate(dcount=Count('date_heure')).filter(
                    date_heure__range=(start_date, end_date))
                print(' stat02 ')
                print(' stat02 ')
                print(' stat02 ')
                print(stat02)
                print(stat02)

            elif int(request.POST['semaine']) == 46:
                start_date = "2018-11-12"
                end_date = "2018-11-19"
                stat = Statisque.objects.filter(date_heure__range=(start_date, end_date)).values('id', 'date_heure',
                                                                                                 'idUser',
                                                                                                 'idUser__nom',
                                                                                                 'idUser__prenom',
                                                                                                 'idUser__civilite',
                                                                                                 'idUser__dateNaiss')

                # stat01 = Statisque.objects.filter(date_heure__range=(start_date, end_date)).annotate(dcount=Count('date_heure')).dates('date_heure', 'day').annotate(c=Count('id'))

                abscisse = Statisque.objects.filter(date_heure__range=(start_date, end_date)).dates('date_heure', 'day')
                ordonnees = Statisque.objects.filter(date_heure__range=(start_date, end_date)).annotate(
                    c=Count('id')).dates('date_heure', 'day').annotate(c=Count('date_heure'))
                print(' abscisse ')
                print(' abscisse ')
                print(abscisse)
                print(abscisse)
                print(' ordonnees ')
                print(' ordonnees ')
                print(ordonnees)
                print(ordonnees)

                stat0001 = Statisque.objects.extra(
                    select={
                        'valeur': "SELECT *, COUNT(date_heure) FROM users_statisque GROUP BY date_heure"
                    }
                )

                stat02 = Statisque.objects.values('date_heure').annotate(dcount=Count('date_heure')).filter(
                    date_heure__range=(start_date, end_date))
                print(' stat02 ')
                print(' stat02 ')
                print(' stat02 ')
                print(stat02)
                print(stat02)

            elif int(request.POST['semaine']) == 47:
                start_date = "2018-11-19"
                end_date = "2018-11-26"
                stat = Statisque.objects.filter(date_heure__range=(start_date, end_date)).values('id', 'date_heure',
                                                                                                 'idUser',
                                                                                                 'idUser__nom',
                                                                                                 'idUser__prenom',
                                                                                                 'idUser__civilite',
                                                                                                 'idUser__dateNaiss')

                # stat01 = Statisque.objects.filter(date_heure__range=(start_date, end_date)).annotate(dcount=Count('date_heure')).dates('date_heure', 'day').annotate(c=Count('id'))

                abscisse = Statisque.objects.filter(date_heure__range=(start_date, end_date)).dates('date_heure', 'day')
                ordonnees = Statisque.objects.filter(date_heure__range=(start_date, end_date)).annotate(
                    c=Count('id')).dates('date_heure', 'day').annotate(c=Count('date_heure'))
                print(' abscisse ')
                print(' abscisse ')
                print(abscisse)
                print(abscisse)
                print(' ordonnees ')
                print(' ordonnees ')
                print(ordonnees)
                print(ordonnees)

                stat0001 = Statisque.objects.extra(
                    select={
                        'valeur': "SELECT *, COUNT(date_heure) FROM users_statisque GROUP BY date_heure"
                    }
                )

                stat02 = Statisque.objects.values('date_heure').annotate(dcount=Count('date_heure')).filter(
                    date_heure__range=(start_date, end_date))
                print(' stat02 ')
                print(' stat02 ')
                print(' stat02 ')
                print(stat02)
                print(stat02)
            elif int(request.POST['semaine']) == 48:
                start_date = "2018-11-26"
                end_date = "2018-12-03"
                stat = Statisque.objects.filter(date_heure__range=(start_date, end_date)).values('id', 'date_heure',
                                                                                                 'idUser',
                                                                                                 'idUser__nom',
                                                                                                 'idUser__prenom',
                                                                                                 'idUser__civilite',
                                                                                                 'idUser__dateNaiss')

                # stat01 = Statisque.objects.filter(date_heure__range=(start_date, end_date)).annotate(dcount=Count('date_heure')).dates('date_heure', 'day').annotate(c=Count('id'))

                abscisse = Statisque.objects.filter(date_heure__range=(start_date, end_date)).dates('date_heure', 'day')
                ordonnees = Statisque.objects.filter(date_heure__range=(start_date, end_date)).annotate(
                    c=Count('id')).dates('date_heure', 'day').annotate(c=Count('date_heure'))
                print(' abscisse ')
                print(' abscisse ')
                print(abscisse)
                print(abscisse)
                print(' ordonnees ')
                print(' ordonnees ')
                print(ordonnees)
                print(ordonnees)

                stat0001 = Statisque.objects.extra(
                    select={
                        'valeur': "SELECT *, COUNT(date_heure) FROM users_statisque GROUP BY date_heure"
                    }
                )

                stat02 = Statisque.objects.values('date_heure').annotate(dcount=Count('date_heure')).filter(
                    date_heure__range=(start_date, end_date))
                print(' stat02 ')
                print(' stat02 ')
                print(' stat02 ')
                print(stat02)
                print(stat02)

            elif int(request.POST['semaine']) == 49:

                start_date = "2018-12-03"
                end_date = "2018-12-10"
                stat = Statisque.objects.filter(date_heure__range=(start_date, end_date)).values('id', 'date_heure',
                                                                                                 'idUser',
                                                                                                 'idUser__nom',
                                                                                                 'idUser__prenom',
                                                                                                 'idUser__civilite',
                                                                                                 'idUser__dateNaiss')

                # stat01 = Statisque.objects.filter(date_heure__range=(start_date, end_date)).annotate(dcount=Count('date_heure')).dates('date_heure', 'day').annotate(c=Count('id'))

                abscisse = Statisque.objects.filter(date_heure__range=(start_date, end_date)).dates('date_heure', 'day')
                ordonnees = Statisque.objects.filter(date_heure__range=(start_date, end_date)).annotate(
                    c=Count('id')).dates('date_heure', 'day').annotate(c=Count('date_heure'))
                print(' abscisse ')
                print(' abscisse ')
                print(abscisse)
                print(abscisse)
                print(' ordonnees ')
                print(' ordonnees ')
                print(ordonnees)
                print(ordonnees)

                stat0001 = Statisque.objects.extra(
                    select={
                        'valeur': "SELECT *, COUNT(date_heure) FROM users_statisque GROUP BY date_heure"
                    }
                )

                stat02 = Statisque.objects.values('date_heure').annotate(dcount=Count('date_heure')).filter(
                    date_heure__range=(start_date, end_date))
                print(' stat02 ')
                print(' stat02 ')
                print(' stat02 ')
                print(stat02)
                print(stat02)


            elif int(request.POST['semaine']) == 50:
                start_date = "2018-12-10"
                end_date = "2018-12-17"
                stat = Statisque.objects.filter(date_heure__range=(start_date, end_date)).values('id', 'date_heure',
                                                                                                 'idUser',
                                                                                                 'idUser__nom',
                                                                                                 'idUser__prenom',
                                                                                                 'idUser__civilite',
                                                                                                 'idUser__dateNaiss')

                # stat01 = Statisque.objects.filter(date_heure__range=(start_date, end_date)).annotate(dcount=Count('date_heure')).dates('date_heure', 'day').annotate(c=Count('id'))

                abscisse = Statisque.objects.filter(date_heure__range=(start_date, end_date)).dates('date_heure', 'day')
                ordonnees = Statisque.objects.filter(date_heure__range=(start_date, end_date)).annotate(
                    c=Count('id')).dates('date_heure', 'day').annotate(c=Count('date_heure'))
                print(' abscisse ')
                print(' abscisse ')
                print(abscisse)
                print(abscisse)
                print(' ordonnees ')
                print(' ordonnees ')
                print(ordonnees)
                print(ordonnees)

                stat0001 = Statisque.objects.extra(
                    select={
                        'valeur': "SELECT *, COUNT(date_heure) FROM users_statisque GROUP BY date_heure"
                    }
                )

                stat02 = Statisque.objects.values('date_heure').annotate(dcount=Count('date_heure')).filter(
                    date_heure__range=(start_date, end_date))
                print(' stat02 ')
                print(' stat02 ')
                print(' stat02 ')
                print(stat02)
                print(stat02)

            elif int(request.POST['semaine']) == 51:
                start_date = "2018-12-17"
                end_date = "2018-12-24"
                stat = Statisque.objects.filter(date_heure__range=(start_date, end_date)).values('id', 'date_heure',
                                                                                                 'idUser',
                                                                                                 'idUser__nom',
                                                                                                 'idUser__prenom',
                                                                                                 'idUser__civilite',
                                                                                                 'idUser__dateNaiss')

                # stat01 = Statisque.objects.filter(date_heure__range=(start_date, end_date)).annotate(dcount=Count('date_heure')).dates('date_heure', 'day').annotate(c=Count('id'))

                abscisse = Statisque.objects.filter(date_heure__range=(start_date, end_date)).dates('date_heure', 'day')
                ordonnees = Statisque.objects.filter(date_heure__range=(start_date, end_date)).annotate(
                    c=Count('id')).dates('date_heure', 'day').annotate(c=Count('date_heure'))
                print(' abscisse ')
                print(' abscisse ')
                print(abscisse)
                print(abscisse)
                print(' ordonnees ')
                print(' ordonnees ')
                print(ordonnees)
                print(ordonnees)

                stat0001 = Statisque.objects.extra(
                    select={
                        'valeur': "SELECT *, COUNT(date_heure) FROM users_statisque GROUP BY date_heure"
                    }
                )

                stat02 = Statisque.objects.values('date_heure').annotate(dcount=Count('date_heure')).filter(
                    date_heure__range=(start_date, end_date))
                print(' stat02 ')
                print(' stat02 ')
                print(' stat02 ')
                print(stat02)
                print(stat02)

            elif int(request.POST['semaine']) == 52:

                start_date = "2018-12-24"
                end_date = "2018-12-31"
                stat = Statisque.objects.filter(date_heure__range=(start_date, end_date)).values('id', 'date_heure',
                                                                                                 'idUser',
                                                                                                 'idUser__nom',
                                                                                                 'idUser__prenom',
                                                                                                 'idUser__civilite',
                                                                                                 'idUser__dateNaiss')

                # stat01 = Statisque.objects.filter(date_heure__range=(start_date, end_date)).annotate(dcount=Count('date_heure')).dates('date_heure', 'day').annotate(c=Count('id'))

                abscisse = Statisque.objects.filter(date_heure__range=(start_date, end_date)).dates('date_heure', 'day')
                ordonnees = Statisque.objects.filter(date_heure__range=(start_date, end_date)).annotate(
                    c=Count('id')).dates('date_heure', 'day').annotate(c=Count('date_heure'))
                print(' abscisse ')
                print(' abscisse ')
                print(abscisse)
                print(abscisse)
                print(' ordonnees ')
                print(' ordonnees ')
                print(ordonnees)
                print(ordonnees)

                stat0001 = Statisque.objects.extra(
                    select={
                        'valeur': "SELECT *, COUNT(date_heure) FROM users_statisque GROUP BY date_heure"
                    }
                )

                stat02 = Statisque.objects.values('date_heure').annotate(dcount=Count('date_heure')).filter(
                    date_heure__range=(start_date, end_date))
                print(' stat02 ')
                print(' stat02 ')
                print(' stat02 ')
                print(stat02)
                print(stat02)


            return render(request, 'tables12.html', locals())



def login(request):
    request.session.flush()
    return render(request, 'login.html')

def blank(request):

    if request.session.get('prenom') is None:
        print(' DANS DANS ')
        return render(request, 'login.html')
    else:
        nbAbonnees = utilisateur2.objects.count()

        employess = employers.objects.all()
        nbEmployess = employers.objects.count()


        return render(request, 'blank.html', locals())


def table(request):

    if request.session.get('prenom') is None:
        print(' DANS DANS ')
        return render(request, 'login.html')
    else:
        employess = employers.objects.all()
        nbEmployess = employers.objects.count()
        cards = personne_essaie.objects.all()
        return render(request, 'tables.html',  locals())

def logout_account(request):

    emails = request.POST.get('email', '')
    passw = request.POST.get('password', '')
    request.session.flush()
    return render(request, 'login.html', {})



def login_account(request):



    #if request.session.get('prenom') is None:
    #    print(' DANS DANS ')
    #    return render(request, 'login.html')
    #else:

    print(" request.session.get('prenom') ")
    print(" request.session.get('prenom') ")
    print(request.session.get('prenom'))
    print(request.session.get('prenom'))

    emails = request.POST.get('email')
    passw = request.POST.get('password')
    print(emails)
    print(passw)
    if adminss.objects.filter(email=emails, password=passw, is_active=True).count() == 1:
        print(" COOOL ")
        print(" COOOL ")
        print(" COOOL ")
        print(" COOOL ")
        print(" COOOL ")
        print(" COOOL ")
        print(" COOOL ")

        adddd = adminss.objects.filter(email=emails, password=passw, is_active=True).count()
        print(adddd)

        adminsss = adminss.objects.get(email=emails, password=passw)

        request.session['prenom'] = adminsss.prenom
        request.session['nom'] = adminsss.nom
        request.session['id'] = adminsss.id

        employess = employers.objects.all()
        nbEmployess = employers.objects.count()

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





        abonnesss = Paiement.objects.all().values('idPaiement', 'date_debut', 'date_fin', 'idUser','idUser__prenom','idUser__nom',
                                                  'idUser__civilite', 'idUser__dateNaiss', 'idUser__lieuNaiss','idUser__adresse','idUser__ville','idUser__email',
                                                  'idUser__profession','idUser__prenom1','idUser__nom1','idUser__telephone1','idUser__prenom2','idUser__nom2',
                                                  'idUser__telephone2','idUser__telephone','idUser__photo','idUser__id_typeabonnement',
                                                  'nbseances_en_cours', 'nbseances_total', 'dateencours',
                                                  'date_autorisation', 'datebadge')
        print(" abonnesss ")
        #print(abonnesss)

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
        request.session.flush()
        error = 'Le mail ou le mot de passe est incorrect.'
        return render(request, 'login.html', {'error': error})


def nouveauInscrit(request):


    if request.session.get('prenom') is None:
        print(' DANS DANS ')
        return render(request, 'login.html')
    else:

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


        return render(request, 'tables14.html', locals())

def dashboard(request):

    print('SESSION ')
    print('SESSION ')
    print('SESSION ')

    print(request.session.get('prenom'))
    print(request.session.get('nom'))
    print(request.session.get('id'))

    #if request.session.get('prenom')=="None" or request.session.get('nom')=="None" or request.session.get('id')=="None":
    if request.session.get('prenom') is None:
        print(' DANS DANS ')
        return render(request, 'login.html')
    else:


        print('ELSE ')
        print('ELSE ')
        print('ELSE ')

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
                                                  'date_autorisation', 'datebadge')
        print(" abonnesss ")
        #print(abonnesss)

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
            datebadge__range=(datefin1,datedebut1))

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
            datebadge__range=(datefin1,datedebut1)).count()

        return render(request, 'dashboard.html', locals())