from django.db.models import Count
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter
from rest_framework.response import Response
from rest_framework import status
from rest_framework.viewsets import ModelViewSet
from .filters import ProductFilter
from .models import Collection, OrderItem, Product, Review
from .serializer import CollectionSerializer, ProductSerializer, ReviewSerializer

# Create your views here.


class ProductViewSet(ModelViewSet):
    """ Product View Set """
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    # fot get info about filtering, go to google and search 'django filters' and click on link that is associated with django site
    filter_backends = [DjangoFilterBackend, SearchFilter]
    # filterset_fields = ['collection_id']
    filterset_class = ProductFilter
    search_fields = ['title', 'description']

    def get_serializer_context(self):
        return {'request': self.request}

    def destroy(self, request, *args, **kwargs):
        if OrderItem.objects.filter(product_id=kwargs['pk']).count() > 0:
            return Response(
                {'error': 'Product cannot be deleted because it is associated with an order item'},
                status=status.HTTP_405_METHOD_NOT_ALLOWED)
        return super().destroy(request, *args, **kwargs)


class CollectionViewSet(ModelViewSet):
    """ Collection view set """
    queryset = Collection.objects.annotate(
        products_count=Count('products')
    ).all()
    serializer_class = CollectionSerializer

    def destroy(self, request, *args, **kwargs):
        if Product.objects.filter(collection_id=kwargs['pk']).count() > 0:
            return Response(
                {'error': 'This collection contain some product in it and deletion function is not available!'},
                status=status.HTTP_204_NO_CONTENT
            )
        return super().destroy(request, *args, **kwargs)


class ReviewViewSet(ModelViewSet):
    """ Review view set """
    serializer_class = ReviewSerializer

    def get_serializer_context(self):
        return {'product_id': self.kwargs['product_pk']}

    def get_queryset(self):
        return Review.objects.filter(product_id=self.kwargs['product_pk'])
