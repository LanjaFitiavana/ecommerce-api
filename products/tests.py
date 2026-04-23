from django.test import TestCase
from  rest_framework.test import APITestCase
from rest_framework import status
from  django.urls import reverse
from .models import Product

# Create your tests here.
class TestProducts(APITestCase):
    def setUp(self):
        self.payload_products= {    
            "name" : "testuser",
            "price" : "100.0",
            "quantity" : "10",
            "descriptions" : "this is just test"
        
        }
        

        self.urls = reverse('products-list')
    def test_register_product(self):

        response = self.client.post(self.urls,data=self.payload_products,format='json')
        print(response.data)
        self.assertEqual(response.status_code,status.HTTP_201_CREATED)

    def test_fail_register(self):
        invalid_payload = self.payload_products.copy()
        invalid_payload['price'] = "not-a-number"
        response = self.client.post(self.urls,data=invalid_payload,format='json')
        self.assertEqual(response.status_code,status.HTTP_400_BAD_REQUEST)
        