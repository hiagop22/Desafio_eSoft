from django.db import models
from django.db.models.base import Model

class User(models.Model):
    name = models.CharField(max_length=255)
    surname = models.CharField(max_length=255)
    age = models.PositiveBigIntegerField()
    birth_date = models.DateField()
    email = models.EmailField(max_length=254)


    def __str__(self):
        return self.name