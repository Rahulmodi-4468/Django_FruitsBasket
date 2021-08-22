from django.db import models

# Create your models here.
class Destination():
    id : int
    name : str
    img : str
    price : int
    offer : bool

# use database
class Destination(models.Model):
    name = models.CharField(max_length=100)
    img = models.ImageField(upload_to='pics')
    price = models.IntegerField()
    offer = models.BooleanField(default=False)


class Category(models.Model):
    name = models.CharField(max_length=50)