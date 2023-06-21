from django.db import models

# Create your models here.
class Customer(models.Model):
    name = models.CharField(unique=True, max_length=30)
    address = models.CharField(max_length=120)
    phone = models.IntegerField()
    email = models.EmailField(unique=True)