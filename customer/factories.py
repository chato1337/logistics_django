from faker import Faker

from customer.models import Customer

faker = Faker()

class CustomerFactory:
    def build_customer_JSON(self):
        return {
            "name": faker.name(),
            "address": "string",
            "phone": 2147483647,
            "email": faker.email()
        }
    
    def create_customer(self):
        return Customer.objects.create(**self.build_customer_JSON())
