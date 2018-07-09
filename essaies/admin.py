from django.contrib import admin


from django.contrib import admin
from essaies.models import *


class PersonneEssaiAdmin(admin.ModelAdmin):
    list_display = ('prenom', 'nom',)
    search_fields = ('telephone', 'nom', 'prenom')
    list_filter = ('telephone',)



# class UserFavouriteContactAdmin(adminsss.ModelAdmin):
#     list_display = ('user', 'favouriteconatct',)

admin.site.register(personne_essaie, PersonneEssaiAdmin)


admin.site.site_title = 'Administration de la plateforme HFC'
admin.site.site_header = 'Administration de la plateforme HFC'