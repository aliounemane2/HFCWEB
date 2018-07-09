from django.conf.urls import url
from users.views import *
from users import views as myapp_views



urlpatterns = [

    #url(r'^$', CategorytList.as_view()),


    #url(r'^get_Create_Carte_Favourite/$', myapp_views.get_Create_Carte_Favourite, name='get_Create_Carte_Favourite'),

    url(r'^insertion/$', myapp_views.insertionUser2, name='insertionUser2'),

    #url(r'^listcardInstitutionelEvent/$', myapp_views.listcardInstitutionelEvent, name='listcardInstitutionelEvent'),



]