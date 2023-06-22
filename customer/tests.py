from django.test import TestCase
from rest_framework.test import APITestCase
from rest_framework import status

from customer.factories import CustomerFactory

# Create your tests here.
class CustomerTestCase(APITestCase):
    url = '/api/v1/customer/'

    def test_get_customers(self):
        response = self.client.get(self.url, {}, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_customer(self):
        response = self.client.post(self.url, CustomerFactory().build_customer_JSON(), format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_create_customer_bad(self):
        response = self.client.post(self.url, {}, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_get_customer_by_id(self):
        customer = CustomerFactory().create_customer()
        response = self.client.get(self.url + str(customer.pk) + '/', {}, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)