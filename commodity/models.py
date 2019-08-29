from django.db import models

# Create your models here.


class Commodity(models.Model):
    name = models.CharField(max_length=100)
    brand = models.CharField(max_length=100, blank=True)
    picture = models.ImageField(upload_to="commodity")
    price = models.IntegerField()
    description = models.CharField(max_length=1000, blank=True)
    in_stock = models.IntegerField(blank=True)

    def __str__(self):
        return str(self.name)
