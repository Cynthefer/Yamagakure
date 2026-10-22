from django.db import models
from rulesets.models import Ruleset

class BattlePost(models.Model):
    title = models.CharField(max_length=200)
    ruleset = models.ForeignKey(Ruleset, on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return self.title