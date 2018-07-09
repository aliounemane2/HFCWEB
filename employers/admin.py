from django.contrib import admin


from django.contrib import admin
from employers.models import *


class EmployersAdmin(admin.ModelAdmin):
    list_display = ('prenom', 'nom',)
    search_fields = ('telephone', 'nom', 'prenom')
    list_filter = ('telephone',)


class PointageAdmin(admin.ModelAdmin):
    list_display = ('date_et_heures',)
    search_fields = ('date_et_heures',)
    list_filter = ('date_et_heures',)



# class UserFavouriteContactAdmin(adminsss.ModelAdmin):
#     list_display = ('user', 'favouriteconatct',)

admin.site.register(employers, EmployersAdmin)
admin.site.register(pointage, PointageAdmin)


admin.site.site_title = 'Administration de la plateforme HFC'
admin.site.site_header = 'Administration de la plateforme HFC'