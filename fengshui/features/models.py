from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.


class Event(models.Model):
    name = models.CharField('Event Name', max_length=120)
    event_date = models.DateTimeField('Event Date')
    venue = models.CharField(max_length=120)
    manager = models.CharField(max_length = 60)
    description = models.TextField(blank=True)
    
    def __str__(self):
        return self.name

    
class Direction(models.Model):
    name = models.CharField(max_length=128)
    animal = models.CharField(max_length=30)
    element = models.CharField(max_length=30)
    flower_colour1 = models.CharField(max_length=30)
    flower_colour2 = models.CharField(max_length=30)
    min_num_flowers = models.IntegerField(default=0)
    max_num_flowers = models.IntegerField(default=0)
    vase_colour1 = models.CharField(max_length=30)
    vase_colour2 = models.CharField(max_length=30)
    compass_direction = models.CharField(max_length=30)
    degree_lower = models.IntegerField(
        default=1,
        validators=[MaxValueValidator(360), MinValueValidator(0)]
     )
    degree_upper = models.IntegerField(
        default=1,
        validators=[MaxValueValidator(360), MinValueValidator(0)]
     )
    members = models.ManyToManyField(User, through='Membership')
    
    def __str__(self):
        return self.name
    
class Membership(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    direction = models.ForeignKey(Direction, on_delete=models.CASCADE)
    date_of_birth = models.DateField()
    animal = models.CharField(max_length=120)
