from rest_framework import serializers

from customer.models import Customer
from delivery.serlializers import DeliverySerializer

class CustomerSerializer(serializers.ModelSerializer):
    delivery = DeliverySerializer(many=True)
    class Meta:
        model = Customer
        exclude = []