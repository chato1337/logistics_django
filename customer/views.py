from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.response import Response
from customer.models import Customer
from customer.serializers import CustomerSerializer, CustomerSerializerFlat

# Create your views here.
class CustomerViewSet(viewsets.ModelViewSet):
    queryset = CustomerSerializerFlat.Meta.model.objects.all()
    serializer_class = CustomerSerializerFlat

class CustomerDeliveryViewSet(viewsets.GenericViewSet):
    serializer_class = CustomerSerializer

    def get_queryset(self):
        return self.get_serializer().Meta.model.objects.all()
    
    def list(self, request, pk):
        data = self.get_queryset()
        data = self.get_serializer(data, many=True)

        return Response(data.data)