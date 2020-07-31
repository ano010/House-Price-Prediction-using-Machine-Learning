from django.db import models

# Create your models here.
class house(models.Model):
    location = models.CharField(max_length=50)
    beds = models.CharField(max_length=50),
    baths = models.CharField,
    house_size = models.CharField,
    land_size = models.CharField,
    
    # def __str__(self):
    #     return {
    #         self.location,
    #         self.beds
    #     }