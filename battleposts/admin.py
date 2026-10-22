from django.contrib import admin
from .models import BattlePost

admin.site.register(BattlePost)
class BattlePostAdmin(admin.ModelAdmin):
    list_display = ('title', 'ruleset', 'created_at', 'updated_at')
    search_fields = ('title', 'content')
    list_filter = ('ruleset', 'created_at', 'updated_at')