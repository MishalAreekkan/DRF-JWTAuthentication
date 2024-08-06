from django.db import models

# Create your models here.

class Person(models.Model):
    name = models.CharField(max_length=50)
    place = models.CharField(max_length=50)
    batch = models.IntegerField()