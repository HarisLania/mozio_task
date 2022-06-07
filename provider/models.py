from locale import currency
from django.db import models

# Create your models here.

class Provider(models.Model):
    name = models.CharField(max_length=64)
    phone_number = models.CharField(max_length=64, unique=True)
    email = models.EmailField(max_length=256, unique=True)
    language = models.CharField(max_length=64)
    currency = models.CharField(max_length=64)

    def __str__(self):
        return self.name + " | " + self.phone_number
    
    