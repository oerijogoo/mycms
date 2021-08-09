from django.db import models

# Create your models here.


class Product(models.Model):
    name = models.CharField(max_length=25)
    price = models.FloatField(max_length=10)