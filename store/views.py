from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Product
from .serializer import ProductSerializer

# Create your views here.


@api_view()
def product_list(request):
    """ Returning list of product """
    queryset = Product.objects.select_related('collection').all()
    serializer = ProductSerializer(
        queryset, many=True, context={'request': request})
    return Response(serializer.data)


@api_view()
def product_detail(request, id):
    """ show the detail of product """
    product = get_object_or_404(Product, pk=id)
    serializer = ProductSerializer(product)
    return Response(serializer.data)


@api_view()
def collection_detail(request, pk):
    return Response('OK')
