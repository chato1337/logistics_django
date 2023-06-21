from django.db import models

from customer.models import Customer

# Create your models here.
class Delivery(models.Model):
    name = models.CharField(max_length=35)
    type_vehicle = models.CharField(max_length=20)
    phone = models.IntegerField()
    customer = models.ForeignKey(Customer, related_name="delivery", on_delete=models.CASCADE)
