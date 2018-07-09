from django.contrib import admin
from adminsss.models import *


class AdminAdmin(admin.ModelAdmin):
    list_display = ('prenom', 'nom',)
    search_fields = ('email', 'nom', 'prenom')
    list_filter = ('email',)


admin.site.register(adminss, AdminAdmin)


admin.site.site_title = 'Administration de la plateforme HFC'
admin.site.site_header = 'Administration de la plateforme HFC'