from django.db import models

from delivery.models import Delivery

# Create your models here.
class Package(models.Model):
    weight = models.CharField(max_length=25)
    address_from = models.CharField(max_length=45)
    address_to = models.CharField(max_length=45)
    status = models.CharField(max_length=40)
    delivery = models.ForeignKey(Delivery, related_name="packages", on_delete=models.CASCADE)