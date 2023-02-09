from django.db import models

# Create your models here.
class Buyer(models.Model):

    all_genders = [
        ('male', 'male'),
        ('female', 'female'),
        ('others', 'others')
    ]
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(unique= True)
    password = models.CharField(max_length=100)
    address = models.CharField(max_length=150)
    gender = models.CharField(choices=all_genders, max_length=20)

    def __str__(self):
        return self.first_name
