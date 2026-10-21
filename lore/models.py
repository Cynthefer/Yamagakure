from django.db import models
from django_ckeditor.fields import RichTextField

class House(models.Model):
    name = models.CharField(max_length=100)
    emblem = models.ImageField(upload_to='house_emblems/')

    def __str__(self):
        return self.name

class PowerSystem(models.Model):
    name = models.CharField(max_length=100)
    scale = models.CharField(max_length=100)
    core_concept = models.TextField()
    mechanics = models.TextField()
    limitations = models.TextField()
    
    class Meta:
        db_table = "power_system"
        verbose_name = "Power System"
        verbose_name_plural = "Power Systems"

    def __str__(self):
        return self.name
    
    def save(self, *args, **kwargs):
        if not self.name:
            raise ValueError("Power System must have a name.")
        if not self.scale:
            raise ValueError("Power System must have a scale.")
        if not self.core_concept:
            raise ValueError("Power System must have a core concept.")
        if not self.mechanics:
            raise ValueError("Power System must have mechanics.")
        if not self.limitations:
            raise ValueError("Power System must have limitations.")
        super().save(*args, **kwargs)

class CombatRanks(models.Model):
    class Class(models.TextChoices):
        Lower = 'Lower', 'Lower'
        Intermediate = 'Intermediate', 'Intermediate'
        High = 'High', 'High'
    
    rank = models.CharField(max_length=100)
    class_type = models.CharField(max_length=100, choices=Class.choices)
    
    class Meta:
        db_table = "combat_ranks"
        verbose_name = "Combat Rank"
        verbose_name_plural = "Combat Ranks"

    def __str__(self):
        return self.rank

class CanonEvent(models.Model):
    name = models.CharField(max_length=100)
    date = models.DateField()
    description = RichTextField()
    
    class Meta:
        db_table = "canon_event"
        verbose_name = "Canon Event"
        verbose_name_plural = "Canon Events"

    def __str__(self):
        return self.name