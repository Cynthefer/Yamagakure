from django.db import models
from django_ckeditor_5.fields import CKEditor5Field

class Ruleset(models.Model):
    name = models.CharField(max_length=255)
    description = CKEditor5Field(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name