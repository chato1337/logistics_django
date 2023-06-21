from rest_framework import serializers

from customer.models import Customer
from delivery.serlializers import DeliverySerializer

class CustomerSerializerFlat(serializers.ModelSerializer):
    class Meta:
        model = Customer
        exclude = []

class CustomerSerializer(serializers.ModelSerializer):
    delivery = DeliverySerializer(many=True)
    class Meta:
        model = Customer
        exclude = []
