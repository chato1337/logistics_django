from rest_framework import serializers

from delivery.models import Delivery

class DeliverySerializer(serializers.ModelSerializer):
    class Meta:
        model = Delivery
        exclude = []