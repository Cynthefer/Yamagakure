from django.contrib import admin
from .models import House, PowerSystem, CombatRanks, In_Character_Calendar, Legislature

@admin.register(House)
class HouseAdmin(admin.ModelAdmin):
    list_display = ('name', 'emblem')
    search_fields = ('name',)

@admin.register(PowerSystem)
class PowerSystemAdmin(admin.ModelAdmin):
    list_display = ('name', 'scale', 'core_concept', 'mechanics', 'limitations')
    search_fields = ('name', 'scale')

@admin.register(CombatRanks)
class CombatRanksAdmin(admin.ModelAdmin):
    list_display = ('rank', 'class_type')
    search_fields = ('rank', 'class_type')

admin.site.register(In_Character_Calendar)
admin.site.register(Legislature)