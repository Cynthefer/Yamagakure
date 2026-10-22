from django.db import models
from django_ckeditor_5.fields import CKEditor5Field

class Tiers(models.Model):
    class tier_standard(models.TextChoices):
        RM = 'RM', 'Realistic Melee'
        URM = 'URM', 'Unrealistic Melee'
        MP = 'MP', 'Moderate Power'
        HP = 'HP', 'High Power'
        PC = 'PC', 'Powered Characters'
        UCP = 'UCP', 'Ultra Powered Characters'
    
    name = models.CharField(max_length=255, choices=tier_standard.choices)
    description = models.TextField(blank=True, null=True)
        
class Ruleset(models.Model):
    name = models.CharField(max_length=255)
    tier = models.ForeignKey(Tiers, on_delete=models.CASCADE)
    description = CKEditor5Field(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        verbose_name = 'Ruleset'
        verbose_name_plural = 'Rulesets'

    def __str__(self):
        return self.name