from django.db import models
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

class RegUser(models.Model):
    name = models.CharField(max_length=128)
    date_of_birth = models.DateField()
    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
    )
    zodiac_animal = models.CharField(max_length=120)
    
    def __str__(self):
        return self.name 
    
    
class Direction(models.Model):
    name = models.CharField(max_length=128)
    animal = models.CharField(max_length=30)
    element = models.CharField(max_length=30)
    flower_colour = models.CharField(max_length=30)
    vase_colour = models.CharField(max_length=30)
    compass_direction = models.CharField(max_length=30)
    degree_lower = models.IntegerField(
        default=1,
        validators=[MaxValueValidator(360), MinValueValidator(0)]
     )
    degree_upper = models.IntegerField(
        default=1,
        validators=[MaxValueValidator(360), MinValueValidator(0)]
     )
    members = models.ManyToManyField(RegUser, through='Membership')
    
    def __str__(self):
        return self.name
    
class Membership(models.Model):
    person = models.ForeignKey(RegUser, on_delete=models.CASCADE)
    group = models.ForeignKey(Direction, on_delete=models.CASCADE)
    date_of_birth = models.DateField()
    animal = models.CharField(max_length=120)
