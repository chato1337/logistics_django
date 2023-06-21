from django.test import TestCase
from rest_framework.test import APITestCase
from rest_framework import status

from delivery.factories import DeliveryFactory

# Create your tests here.
class DeliveryTestCase(APITestCase):
    url = '/api/v1/delivery/'
    def test_get_deliveries(self):
        response = self.client.get(self.url, {}, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_delivery(self):
        response = self.client.post(self.url, DeliveryFactory().build_delivery_JSON(), format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_create_delivery_bad(self):
        response = self.client.post(self.url, {}, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)