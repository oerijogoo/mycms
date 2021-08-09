from django.db import models

# Create your models here.


class Project(models.Model):
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    image = models.CharField(max_length=2083)


class Offer(models.Model):
    code = models.CharField(max_length=10)
    describe = models.CharField(max_length=255)
    discount = models.FloatField()
