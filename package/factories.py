from faker import Faker

from delivery.factories import DeliveryFactory

faker = Faker()

class PackageFactory:
    def build_package_JSON(self):
        delivery = DeliveryFactory().build_delivery_JSON()
        return {
            "content": "iphone",
            "weight": "65kg",
            "address_from": "cali",
            "address_to": "bogota",
            "status": "pending",
            "delivery": delivery.pk
        }
