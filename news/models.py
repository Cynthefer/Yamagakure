from django.db import models
from thumbnails.fields import ImageField
from django.contrib.auth import get_user_model
from django_ckeditor_5.fields import CKEditor5Field

class News(models.Model):
    title = models.CharField(max_length=200)
    thumbnail = ImageField()
    restriction = models.IntegerField(help_text="Enter the restriction level for this news item (1-7).")
    content = CKEditor5Field()
    author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return self.title