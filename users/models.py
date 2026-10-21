from django.db import models
from lore.models import House, CombatRanks
from django.contrib.auth.models import AbstractUser

class Honorific(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.title

class Profile(AbstractUser):
    class Classification_Choices(models.TextChoices):
        First = '1', 'Class 1'
        Second = '2', 'Class 2'
        Third = '3', 'Class 3'
        Fourth = '4', 'Class 4'
        Fifth = '5', 'Class 5'
        Sixth = '6', 'Class 6'
        Seventh = '7', 'Class 7'
    
    
    avatar = models.ImageField(upload_to='avatars/', null=True, blank=True)
    house = models.ForeignKey(House, on_delete=models.SET_NULL, null=True, blank=True)
    combat_rank = models.ForeignKey(CombatRanks, on_delete=models.SET_NULL, null=True, blank=True)
    class_level = models.CharField(max_length=1, choices=Classification_Choices.choices, default=Classification_Choices.First)
    bio = models.TextField(blank=True)
    honorifics = models.ManyToManyField(Honorific, blank=True)

    def __str__(self):
        return self.username
    
    def can_view_classified(self, required_class):
        if self.class_level is None:
            return False
        return int(self.class_level) >= required_class
    def can_manage_user_class(self, target_user):
        if self.class_level > 5:
            return True
        if self.class_level <= target_user.class_level:
            return False
        return True