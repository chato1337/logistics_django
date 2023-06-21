from rest_framework import serializers

from delivery.models import Delivery
from package.serializers import PackageSerializer

class DeliverySerializerFlat(serializers.ModelSerializer):
    class Meta:
        model = Delivery
        exclude = []

class DeliverySerializer(serializers.ModelSerializer):
    packages = PackageSerializer(many=True)
    class Meta:
        model = Delivery
        exclude = []
