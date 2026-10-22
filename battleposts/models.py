from django.db import models
from rulesets.models import Ruleset
from thumbnails.fields import ImageField

class BattlePost(models.Model):
    title = models.CharField(max_length=200)
    thumbnail = ImageField(upload_to='battlepost_thumbnails/', blank=True, null=True)
    weather = models.CharField(max_length=100)
    time = models.TimeField()
    Location = models.CharField(max_length=200)
    Temperature = models.IntegerField()
    windspeed = models.IntegerField()
    ruleset = models.ForeignKey(Ruleset, on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return self.title