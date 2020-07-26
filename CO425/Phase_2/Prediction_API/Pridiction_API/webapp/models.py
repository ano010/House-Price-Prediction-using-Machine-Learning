from django.db import models

# Create your models here.
class house(models.Model):
    location = models.CharField(max_length=50)
    beds = models.CharField(max_length=50),
    baths = models.IntegerField,
    house_size = models.FloatField,
    land_size = models.FloatField,
    
    # def __str__(self):
    #     return {
    #         self.location,
    #         self.beds
    #     }