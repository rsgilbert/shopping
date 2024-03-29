from django.db import models
from commodity.models import Commodity
# Create your models here.



class Order(models.Model):
    fullname = models.CharField(max_length=100)
    telephone = models.CharField(max_length=100)
    commodity = models.ForeignKey(to=Commodity, on_delete=models.CASCADE)
    hall = models.CharField(max_length=100)
    room_number = models.CharField(max_length=10)


class OrderHistory(models.Model):
    fullname = models.CharField(max_length=100)
    telephone = models.CharField(max_length=100)
    commodity = models.ForeignKey(to=Commodity, on_delete=models.CASCADE)
    hall = models.CharField(max_length=100)
    room_number = models.CharField(max_length=10)