from faker import Faker

from customer.factories import CustomerFactory
from delivery.models import Delivery

faker = Faker()

class DeliveryFactory:
    def build_delivery_JSON(self):
        customer = CustomerFactory().create_customer()
        return {
            "name": "route1",
            "type_vehicle": "car",
            "phone": 2147483647,
            "customer": customer.pk
        }

    def create_delivery(self):
        return Delivery.objects.create(**self.build_delivery_JSON())