from django.test import TestCase
from rest_framework.test import APITestCase
from rest_framework import status
from .models import Producto

# Test de la aplicación de productos.
class ProductoTests(APITestCase):
    def test_crear_producto(self):
        data = {'nombre': 'Test', 'precio': '99.99'}
        response = self.client.post('/api/productos/', data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_listar_productos(self):
        Producto.objects.create(nombre='P1', precio=10.0)
        response = self.client.get('/api/productos/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

