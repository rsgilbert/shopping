from django.db import models

# Create your models here.


class Commodity(models.Model):
    name = models.CharField(max_length=100)
    brand = models.CharField(max_length=100)
    picture = models.CharField(max_length=255)
    price = models.DecimalField()
    description = models.CharField(max_length=1000)
    in_stock = models.IntegerField()