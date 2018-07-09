from django.contrib import admin
from import_export.admin import ImportExportModelAdmin

from users.models import *


# class UserAdmin(adminsss.ModelAdmin):
class UserAdmin(ImportExportModelAdmin):
    list_display = ('nom', 'prenom', 'email')
    search_fields = ('telephone', 'email')
    list_filter = ('telephone',)





class PaiementAdmin(ImportExportModelAdmin):
    list_display = ('date_debut', 'date_fin',)


class Type_AbonnementAdmin(admin.ModelAdmin):
    list_display = ('nom', 'montant',)
    search_fields = ('nom', 'montant')
    list_filter = ('nom',)


admin.site.register(utilisateur2, UserAdmin)
admin.site.register(Paiement, PaiementAdmin)
admin.site.register(Type_Abonnement, Type_AbonnementAdmin)

admin.site.site_title = 'Administration de la plateforme HFC'
admin.site.site_header = 'Administration de la plateforme HFC'


