from django.contrib import admin
from .models import Continent, State

class ContinentAdmin(admin.ModelAdmin):
    list_display = ('name', 'region', 'land_mass')
    search_fields = ('name', 'region')

class StateAdmin(admin.ModelAdmin):
    list_display = ('name', 'biome', 'capital', 'population', 'area')
    search_fields = ('name', 'biome', 'capital')