from typing import Any
from django.contrib import admin
from django.db.models.query import QuerySet
from django.http.request import HttpRequest
from django.db.models import Count

from . import models


@admin.register(models.Collection)
class CollectionAdmin(admin.ModelAdmin):
    """ Collection admin class """
    list_display = ['title', 'products_count']

    @admin.display(ordering='products_count')
    def products_count(self, collection):
        """ return some extra field from model the actually don't exist on model field"""
        return collection.products_count

    def get_queryset(self, request: HttpRequest) -> QuerySet[Any]:
        return super().get_queryset(request).annotate(
            products_count=Count('product')
        )

# define the admin class


@admin.register(models.Product)
class ProductAdmin(admin.ModelAdmin):
    """ Product admin class """
    list_display = ['title', 'unit_price',
                    'inventory_status', 'collection_title']
    list_editable = ['unit_price']
    list_per_page = 10
    # eager load collection model fields to prevent execute extra queries
    list_select_related = ['collection']

    def collection_title(self, product):
        """ return some specific field from related model """
        return product.collection.title

    # if you want to add sort available to this column, you should add this decorator
    @admin.display(ordering='inventory')
    def inventory_status(self, product):
        """ Customizing inventory field """
        if product.inventory < 10:
            return 'Low'
        return 'OK'

# this is the second way to define admin class
# admin.site.register(models.Product, ProductAdmin)


@admin.register(models.Customer)
class CustomerAdmin(admin.ModelAdmin):
    """ Customer admin class """
    list_display = ['first_name', 'last_name', 'membership']
    list_editable = ['membership']
    ordering = ['first_name', 'last_name']
    list_per_page = 10


@admin.register(models.Order)
class OrderAdmin(admin.ModelAdmin):
    """ OrderAdmin admin class """
    list_display = ['id', 'placed_at', 'customer']
