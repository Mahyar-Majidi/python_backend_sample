from rest_framework import serializers
from decimal import Decimal
from store.models import Collection, Product


class CollectionSerializer(serializers.ModelSerializer):
    """ Collection serializer class """
    class Meta:
        model = Collection
        fields = ['id', 'title']


class ProductSerializer(serializers.ModelSerializer):
    """ Product serializer class """
    class Meta:
        model = Product
        fields = ['id', 'title', 'unit_price', 'price_with_tax', 'collection']
    price_with_tax = serializers.SerializerMethodField(
        method_name='calculate_tax')


    def calculate_tax(self, product: Product):
        return product.unit_price * Decimal(1.1)
