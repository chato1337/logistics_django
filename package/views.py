from django.shortcuts import render
from rest_framework import viewsets

from package.serializers import PackageSerializer

# Create your views here.
class PackageViewSet(viewsets.ModelViewSet):
    serializer_class = PackageSerializer
    queryset = PackageSerializer.Meta.model.objects.all()