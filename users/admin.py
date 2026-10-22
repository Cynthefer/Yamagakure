from django.contrib import admin
from .models import Profile, Honorific

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'first_name', 'last_name', 'house', 'combat_rank', 'class_level')
    search_fields = ('username', 'email', 'first_name', 'last_name')
    list_filter = ('house', 'combat_rank', 'class_level')
@admin.register(Honorific)
