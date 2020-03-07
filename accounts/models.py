from django.db import models
from django.contrib.auth.models import User
from features.models import Direction



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
    
    direction = models.ForeignKey('features.Direction', on_delete=models.CASCADE)

    
    def save(self, *args, **kwargs):
        #improve by making a list of animals in each direction
        if self.zodiac_animal == "Pig" or self.zodiac_animal == "Sheep" or self.zodiac_animal == "Rabbit":
            self.direction = Direction.objects.get(name="North")
        elif self.zodiac_animal == "Tiger" or self.zodiac_animal == "Dog" or self.zodiac_animal == "Horse":
            self.direction = Direction.objects.get(name="East")
        elif self.zodiac_animal == "Ox" or self.zodiac_animal == "Snake" or self.zodiac_animal == "Rooster":
            self.direction = Direction.objects.get(name="South")
        elif self.zodiac_animal == "Dragon" or self.zodiac_animal == "Monkey" or self.zodiac_animal == "Rat":
            self.direction = Direction.objects.get(name="West")      

        # Call save on the superclass.
        return super(Profile, self).save(*args, **kwargs)
    
    def __str__(self):
        return self.name 