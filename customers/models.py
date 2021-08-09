from django.db import models

# Create your models here.


class Customer(models.Model):
    name = models.CharField(max_length=25)
    age = models.PositiveIntegerField(max_length=2)
    county = models.CharField(max_length=25)