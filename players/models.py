from django.db import models


# Create your models here.
class Player(models.Model):
    name = models.CharField(max_length=25)
    age = models.PositiveIntegerField(max_length=2)
    city = models.CharField(max_length=20)
