from django.db import models

# Create your models here.


class Hospital(models.Model):
    name = models.CharField(max_length=255)
    place = models.CharField(max_length=255)
    image = models.CharField(max_length=255)
