from django.shortcuts import render
from rest_framework import viewsets

from delivery.serlializers import DeliverySerializer, DeliverySerializerFlat


class DeliveryViewSet(viewsets.ModelViewSet):
    serializer_class = DeliverySerializerFlat
    queryset = DeliverySerializerFlat.Meta.model.objects.all()