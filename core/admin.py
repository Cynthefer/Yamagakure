from django.contrib import admin
from .models import SiteSettings

@admin.register(SiteSettings)
class SiteSettingsAdmin(admin.ModelAdmin):
    list_display = ('site_name', 'site_description', 'site_logo', 'background_image', 'colors')
    search_fields = ('site_name', 'site_description')
    list_filter = ('site_name',)