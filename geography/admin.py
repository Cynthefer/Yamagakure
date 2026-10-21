from django.contrib import admin
from .models import Continent, State

@admin.register(Continent)
class ContinentAdmin(admin.ModelAdmin):
    list_display = ('name', 'region', 'land_mass')
    search_fields = ('name', 'region')

@admin.register(State)
class StateAdmin(admin.ModelAdmin):
    list_display = ('name', 'biome', 'population',)
    search_fields = ('name', 'biome', 'capital')