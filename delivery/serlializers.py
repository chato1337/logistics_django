from rest_framework import serializers

from delivery.models import Delivery
from package.serializers import PackageSerializer

class DeliverySerializer(serializers.ModelSerializer):
    packages = PackageSerializer(many=True)
    class Meta:
        model = Delivery
        exclude = []