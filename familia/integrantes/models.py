from django.db import models

# Create your models here.


class Personas(models.Model):
    name = models.CharField(max_length=20)
    surname = models.CharField(max_length=20)
    edad = models.IntegerField()
    nacimiento = models.DateField()