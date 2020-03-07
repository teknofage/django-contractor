from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.
    
class Direction(models.Model):
    name = models.CharField(max_length=128)
    animal = models.CharField(max_length=30)
    element = models.CharField(max_length=30)
    flower_colours = models.CharField(max_length=40)
    num_flowers = models.CharField(max_length=40)
    vase_colours = models.CharField(max_length=30)
    compass_direction = models.CharField(max_length=30)
    degree_lower = models.DecimalField(max_digits=5, decimal_places=2
     )
    degree_upper = models.DecimalField(max_digits=5, decimal_places=2
     )
    
    def __str__(self):
        return self.name
    

