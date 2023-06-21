from django.shortcuts import render
from rest_framework import viewsets

from customer.models import Customer
from customer.serializers import CustomerSerializer

# Create your views here.
class CustomerViewSet(viewsets.ModelViewSet):
    queryset = CustomerSerializer.Meta.model.objects.all()
    serializer_class = CustomerSerializer
