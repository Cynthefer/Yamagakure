from django.db import models

class SiteSettings(models.Model):
    site_name = models.CharField(max_length=255)
    site_description = models.TextField()
    site_logo = models.ImageField(upload_to='site_logos/')
    background_image = models.ImageField(upload_to='background_images/')
    colors = models.JSONField(default=dict)  # Store colors as a JSON object

    def __str__(self):
        return self.site_name