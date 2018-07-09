"""HFCWEB URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from users.views import *
from users import views as myapp_views
from essaies.views import *
from employers.views import *
from employers import views as myapp_views1

from adminsss.views import *

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [

    url(r'^admin/', admin.site.urls),
    url(r'^users/', include('users.urls')),

    #### URL de l'API de la synchronisation

    url(r'^insertionUsers/$', myapp_views.insertionUser2, name='insertionUser2'),
    url(r'^insertionDatabase/$', myapp_views.insertionDatabase, name='insertionDatabase'),

    url(r'^insertionType_Abonnement/$', insertionType_Abonnement, name='insertionType_Abonnement'),
    url(r'^insertionDatabaseTypeAbonnement/$', insertionDatabaseTypeAbonnement, name='insertionDatabaseTypeAbonnement'),

    url(r'^insertionPaiement/$', insertionPaiement, name='insertionPaiement'),
    url(r'^insertionDatabasePaiement/$', insertionDatabasePaiement, name='insertionDatabasePaiement'),

    url(r'^insertionStatistique/$', insertionStatistique, name='insertionStatistique'),
    url(r'^insertionDatabaseStatistique/$', insertionDatabaseStatistique, name='insertionDatabaseStatistique'),


    url(r'^insertionEmployers/$', myapp_views1.insertionEmployers, name='insertionEmployers'),
    url(r'^insertionEmployersDatabase/$', myapp_views1.insertionEmployersDatabase, name='insertionEmployersDatabase'),

    url(r'^insertionPointage/$', myapp_views1.insertionPointage, name='insertionPointage'),
    url(r'^insertionPointageDatabase/$', myapp_views1.insertionPointageDatabase, name='insertionPointageDatabase'),

    url(r'^insertionEssaie/$', insertionEssaie, name='insertionEssaie'),
    url(r'^insertionEssaieDatabase/$', insertionEssaieDatabase, name='insertionEssaieDatabase'),

    url(r'^insertionParrainage/$', insertionParrainage, name='insertionParrainage'),
    url(r'^insertionDatabaseParrainnage/$', insertionDatabaseParrainnage, name='insertionDatabaseParrainnage'),


    url(r'^nombreAbonnees/$', nombreAbonnees, name='nombreAbonnees'),
    url(r'^nombrePersonneEssai/$', nombrePersonneEssai, name='nombrePersonneEssai'),

    url(r'^login/$', login, name='login'),
    url(r'^forgetpassword/$', forgetpassword, name='forgetpassword'),
    url(r'^inscription/$', inscription, name='inscription'),
    url(r'^send_email_password/$', send_email_password, name='send_email_password'),
    url(r'^$', login, name='login'),
    url(r'^login_account/$', login_account, name='login_account'),
    url(r'^blank/$', blank, name='blank'),
    url(r'^table/$', table, name='table'),
    url(r'^table2/$', abonnes, name='abonnes'),
    url(r'^table3/$', nombreAbonnees30, name='nombreAbonnees30'),
    url(r'^table4/$', employersall, name='employersall'),
    url(r'^table5/$', employersalls, name='employersalls'),
    url(r'^table7/$', table7, name='table7'),
    #url(r'^table6/$', table6, name='table6'),
    url(r'^edit_emp/$', edit_emp, name='edit_emp'),
    url(r'^edit_user/$', edit_user, name='edit_user'),
    url(r'^edit_emp_valid/$', edit_emp_valid, name='edit_emp_valid'),
    url(r'^edit_user_valid/$', edit_user_valid, name='edit_user_valid'),
    url(r'^dashboard/$', dashboard, name='dashboard'),
    url(r'^calculdutemps/$', calculdutemps, name='calculdutemps'),
    url(r'^logout_account/$', logout_account, name='logout_account'),
    url(r'^statistique/$', statistique, name='statistique'),
    url(r'^statDetailAbonne/$', statDetailAbonne, name='statDetailAbonne'),
    url(r'^statParSemaine/$', statParSemaine, name='statParSemaine'),
    url(r'^statParJour/$', statParJour, name='statParJour'),
    url(r'^statParJour1/$', statParJour1, name='statParJour1'),
    url(r'^statHeuresdaff/$', statHeuresdaff, name='statHeuresdaff'),
    url(r'^30derniersJours/$', statParMois30derniersJours, name='statParMois30derniersJours'),
    url(r'^table007/$', table007, name='table007'),
    url(r'^statTrancheDate/$', statTrancheDate, name='statTrancheDate'),
    url(r'^statParMois/$', statParMois, name='statParMois'),
    url(r'^statParMoisForms/$', statParMoisForms, name='statParMoisForms'),
    url(r'^inscription1/$', inscription1, name='inscription1'),
    url(r'^inscription2/$', inscription2, name='inscription2'),
    url(r'^hebdomadaires/$', hebdomadaires, name='hebdomadaires'),
    url(r'^hebdomadaires1/$', hebdomadaires1, name='hebdomadaires1'),
    url(r'^statCroises/$', statCroises, name='statCroises'),
    url(r'^statCroises1/$', statCroises1, name='statCroises1'),
    url(r'^parrainage/$', parrainage, name='parrainage'),
    url(r'^nouveauInscrit/$', nouveauInscrit, name='nouveauInscrit'),
    url(r'^idcarte/$', idcarte, name='idcarte'),
    url(r'^insertionIdCarte/$', insertionIdCarte, name='insertionIdCarte'),
    url(r'^parrainage1/$', parrainage1, name='parrainage1'),
    url(r'^statistique4/$', statistique4, name='statistique4'),



    url(r'^insertionEmployerss/$', insertionEmployerss, name='insertionEmployerss'),
    url(r'^forms/$', forms, name='forms'),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


