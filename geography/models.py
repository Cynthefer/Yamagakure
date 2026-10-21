from django.db import models
from lore.models import House

class Continent(models.Model):
    class Regions(models.TextChoices):
        Center = 'Center', 'Center'
        East = 'East', 'East'
        North = 'North', 'North'
        West = 'West', 'West'
        South = 'South', 'South'
    
    name = models.CharField(max_length=100)
    map = models.ImageField(upload_to='continent_maps/', null=True, blank=True)
    region = models.CharField(max_length=100, choices=Regions.choices, null=True, blank=True)
    land_mass = models.FloatField(help_text="Land mass in square kilometers")
    description = models.TextField(null=True, blank=True)
    
    class Meta:
        db_table = "continent"
        verbose_name = "Continent"
        verbose_name_plural = "Continents"

    def __str__(self):
        return self.name
    
    def save(self, *args, **kwargs):
        if self.land_mass < 0:
            raise ValueError("Land mass cannot be negative.")
        if self.region not in dict(self.Regions.choices):
            raise ValueError(f"Region must be one of the following: {', '.join(dict(self.Regions.choices).keys())}.")
        if self.map and not self.map.name.lower().endswith(('.png', '.jpg', '.jpeg')):
            raise ValueError("Map must be an image file (PNG, JPG, JPEG).")
        if self.pk > 5:
            raise ValueError("Cannot create more than 5 continents.")
        super().save(*args, **kwargs)

class State(models.Model):
    class Biomes(models.TextChoices):
        Desert = 'Desert', 'Desert'
        Forest = 'Forest', 'Forest'
        Grassland = 'Grassland', 'Grassland'
        Tundra = 'Tundra', 'Tundra'
        Wetland = 'Wetland', 'Wetland'
        Rainforest = 'Rainforest', 'Rainforest'
        Savanna = 'Savanna', 'Savanna'
        Mediterranean = 'Mediterranean', 'Mediterranean'
        DecidousForest = 'Deciduous Forest', 'Deciduous Forest'
        BorealForest = 'Boreal Forest', 'Boreal Forest'
        Coastal = 'Coastal', 'Coastal'
        Mountain = 'Mountain', 'Mountain'
        Riparian = 'Riparian', 'Riparian'
        Polar = 'Polar', 'Polar'
    
    class CardinalDirections(models.TextChoices):
        North = 'North', 'North'
        South = 'South', 'South'
        East = 'East', 'East'
        West = 'West', 'West'
        Northeast = 'Northeast', 'Northeast'
        Northwest = 'Northwest', 'Northwest'
        Southeast = 'Southeast', 'Southeast'
        Southwest = 'Southwest', 'Southwest'
    
    name = models.CharField(max_length=100)
    map = models.ImageField(upload_to='state_maps/', null=True, blank=True)
    governor = models.ForeignKey(House, on_delete=models.SET_NULL, null=True, blank=True, related_name='governed_states')
    continent = models.ForeignKey(Continent, on_delete=models.CASCADE, related_name='states')
    biome = models.CharField(max_length=100, choices=Biomes.choices, null=True, blank=True)
    direction = models.CharField(max_length=100, choices=CardinalDirections.choices, null=True, blank=True)
    population = models.PositiveIntegerField()
    land_mass = models.FloatField(help_text="Land mass in square kilometers")
    
    class Meta:
        db_table = "state"
        verbose_name = "State"
        verbose_name_plural = "States"

    def __str__(self):
        return self.name
    
    def save(self, *args, **kwargs):
        if self.land_mass < 0:
            raise ValueError("Land mass cannot be negative.")
        if self.population < 0:
            raise ValueError("Population cannot be negative.")
        if self.biome not in dict(self.Biomes.choices):
            raise ValueError(f"Biome must be one of the following: {', '.join(dict(self.Biomes.choices).keys())}.")
        if self.map and not self.map.name.lower().endswith(('.png', '.jpg', '.jpeg')):
            raise ValueError("Map must be an image file (PNG, JPG, JPEG).")
        super().save(*args, **kwargs)