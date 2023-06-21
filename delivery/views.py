from django.shortcuts import render
from rest_framework import viewsets

from delivery.serlializers import DeliverySerializer


class DeliveryViewSet(viewsets.ModelViewSet):
    serializer_class = DeliverySerializer
    queryset = DeliverySerializer.Meta.model.objects.all()