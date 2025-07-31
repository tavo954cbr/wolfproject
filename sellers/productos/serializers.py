from rest_framework import serializers
from .models import Producto

# Serializador del producto.
class ProductoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Producto
        fields = '__all__'
