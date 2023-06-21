from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.response import Response
from delivery.serlializers import DeliverySerializer, DeliverySerializerFlat


class DeliveryViewSet(viewsets.ModelViewSet):
    serializer_class = DeliverySerializerFlat
    queryset = DeliverySerializerFlat.Meta.model.objects.all()

class DeliveryPackagesViewSet(viewsets.GenericViewSet):
    serializer_class = DeliverySerializer

    def get_queryset(self):
        return self.get_serializer().Meta.model.objects.all()
    
    def list(self, request, pk):
        data = self.get_queryset()
        data = self.get_serializer(data, many=True)

        return Response(data.data)