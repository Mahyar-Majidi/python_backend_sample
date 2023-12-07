from django.shortcuts import get_object_or_404
from django.db.models import Count
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet
from .models import Collection, Product
from .serializer import CollectionSerializer, ProductSerializer

# Create your views here.


class ProductViewSet(ModelViewSet):
    """ Product View Set """
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = 'id'

    def get_serializer_class(self):
        return {'request': self.request}

    def delete(self, request, id):
        product = get_object_or_404(Product, pk=id)
        if product.orderitems.count() > 0:
            return Response({'error': 'Product cannot be deleted because it is associated with an order item'}, status=status.HTTP_405_METHOD_NOT_ALLOWED)
        product.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class CollectionViewSet(ModelViewSet):
    """ Collection view set """
    queryset = Collection.objects.annotate(
        products_count=Count('products').all()
    )
    serializer_class = CollectionSerializer

    def delete(self, request, pk):
        collection = get_object_or_404(Collection, pk=pk)
        if collection.products.count() > 0:
            return Response(
                {'error': 'This collection contain some product in it and deletion function is not available!'},
                status=status.HTTP_204_NO_CONTENT
            )
        collection.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
