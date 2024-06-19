from django.contrib import admin

from main.models import Person, Rota, Vzvod


class PersonAdmin(admin.ModelAdmin):
    list_display = ['surname','rota', 'vzvod']


admin.site.register(Person, PersonAdmin)

class RotaAdmin(admin.ModelAdmin):
    pass


admin.site.register(Rota, RotaAdmin)

class VzvodAdmin(admin.ModelAdmin):
    list_display = ['name','rota']


admin.site.register(Vzvod, VzvodAdmin)