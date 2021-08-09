from django.db import models

# Create your models here.


class Mkulima(models.Model):
    name = models.TextField(max_length=30)
    description = models.TextField(max_length=50)
    age = models.CharField(max_length=2)
