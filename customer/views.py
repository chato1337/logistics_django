from django.shortcuts import render
from rest_framework import viewsets

from customer.models import Customer
from customer.serializers import CustomerSerializer, CustomerSerializerFlat

# Create your views here.
class CustomerViewSet(viewsets.ModelViewSet):
    queryset = CustomerSerializerFlat.Meta.model.objects.all()
    serializer_class = CustomerSerializerFlat
