from django.contrib import admin
from .models import House, PowerSystem, CombatRanks

class HouseAdmin(admin.ModelAdmin):
    list_display = ('name', 'emblem')
    search_fields = ('name',)

class PowerSystemAdmin(admin.ModelAdmin):
    list_display = ('name', 'scale', 'core_concept', 'mechanics', 'limitations')
    search_fields = ('name', 'scale')

class CombatRanksAdmin(admin.ModelAdmin):
    list_display = ('rank', 'class_type')
    search_fields = ('rank', 'class_type')