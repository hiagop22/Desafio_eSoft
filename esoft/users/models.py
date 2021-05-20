from django.db import models
from django.db.models.base import Model

class User(models.Model):
    name = models.CharField(verbose_name='Nome', max_length=255)
    surname = models.CharField(verbose_name='Sobrenome', max_length=255)
    age = models.PositiveBigIntegerField(verbose_name='Idade')
    birth_date = models.DateField(verbose_name='Data de nascimento')
    email = models.EmailField(verbose_name='E-mail', max_length=254)


    def __str__(self):
        return self.name