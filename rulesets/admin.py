from django.contrib import admin
from .models import Ruleset

@admin.register(Ruleset)
class RulesetAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')