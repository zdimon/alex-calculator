from django.contrib import admin

from main.models import Person, Rota, Vzvod, Instructor, Position, Position2Person


class PersonAdmin(admin.ModelAdmin):
    list_display = ['surname','rota', 'vzvod', 'position']


admin.site.register(Person, PersonAdmin)

class RotaAdmin(admin.ModelAdmin):
    pass


admin.site.register(Rota, RotaAdmin)

class VzvodAdmin(admin.ModelAdmin):
    list_display = ['name','rota']


admin.site.register(Vzvod, VzvodAdmin)

class InstructorAdmin(admin.ModelAdmin):
    list_display = ['name','phone', 'can_edit']


admin.site.register(Instructor, InstructorAdmin)

class PositionAdmin(admin.ModelAdmin):
    list_display = ['name', 'color']


admin.site.register(Position, PositionAdmin)


class Position2PersonAdmin(admin.ModelAdmin):
    list_display = ['position', 'person', 'editor', 'created_at']


admin.site.register(Position2Person, Position2PersonAdmin)
