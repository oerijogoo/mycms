from django.db import models

# Create your models here.


class Worker(models.Model):
    name = models.CharField(max_length=25)
    county = models.CharField(max_length=25)
    age = models.CharField(max_length=2)
    office = models.CharField(max_length=30)
