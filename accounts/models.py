from django.db import models
from django.contrib.auth.models import User



# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=128)
    date_of_birth = models.DateField()
    
    zodiac_animal_choices = [
        ("Rat", "Rat"),
        ("Ox", "Ox"),
        ("Tiger", "Tiger"),
        ("Rabbit", "Rabbit"),
        ("Dragon", "Dragon"),
        ("Snake", "Snake"),
        ("Horse", "Horse"),
        ("Sheep", "Sheep"),
        ("Monkey", "Monkey"),
        ("Rooster", "Rooster"),
        ("Dog", "Dog"),
        ("Pig", "Pig"),
    ]
    zodiac_animal = models.CharField(
        max_length=7,
        choices = zodiac_animal_choices,
        default = "Rat",
        )
    GENDER_CHOICES = [
    ('M', 'Male'),
    ('F', 'Female'),
    ]
    gender = models.CharField(
        max_length=1,
        choices = GENDER_CHOICES,
        default = "F",
    )
    
    def __str__(self):
        return self.name 