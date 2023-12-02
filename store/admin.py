from typing import Any
from django.contrib import admin
from django.db.models.query import QuerySet
from django.http.request import HttpRequest
from django.db.models import Count
from django.urls import reverse
from django.utils.html import format_html, urlencode

from . import models


@admin.register(models.Collection)
class CollectionAdmin(admin.ModelAdmin):
    """ Collection admin class """
    list_display = ['title', 'products_count']

    @admin.display(ordering='products_count')
    def products_count(self, collection):
        """ return some extra field from model the actually don't exist on model field"""
        url = (reverse('admin:store_product_changelist') + '?' + urlencode({
            'collection_id': collection.id
        }))
        return format_html('<a href={}>{}</a>', url, collection.products_count)

    def get_queryset(self, request: HttpRequest) -> QuerySet[Any]:
        return super().get_queryset(request).annotate(
            products_count=Count('product')
        )

# define the admin class


class InventoryFilter(admin.SimpleListFilter):
    """ Create customize search in admin control panel for Product """
    title = 'inventory'
    parameter_name = 'inventory'

    def lookups(self, request: Any, model_admin: Any) -> list[tuple[Any, str]]:
        return [
            ('<10', 'Low')
        ]

    def queryset(self, request: Any, queryset: QuerySet[Any]):
        if self.value() == "<10":
            return queryset.filter(inventory__lt=10)


@admin.register(models.Product)
class ProductAdmin(admin.ModelAdmin):
    """ Product admin class """
    list_display = ['title', 'unit_price',
                    'inventory_status', 'collection_title']
    list_editable = ['unit_price']
    list_filter = ['collection', 'last_update', InventoryFilter]
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
    list_display = ['first_name', 'last_name', 'membership', 'order_count']
    list_editable = ['membership']
    ordering = ['first_name', 'last_name']
    search_fields = ['first_name__istartswith', 'last_name__istartswith']
    list_per_page = 10

    @admin.display(ordering='order_count')
    def order_count(self, customer):
        """ Provide the order_count field """
        url = reverse('admin:store_order_changelist') + "?" + urlencode({
            'customer_id': customer.id
        })
        return format_html("<a href={}>{}</a>", url, customer.order_count)

    def get_queryset(self, request: HttpRequest) -> QuerySet[Any]:
        return super().get_queryset(request).annotate(
            order_count=Count('order')
        )


@admin.register(models.Order)
class OrderAdmin(admin.ModelAdmin):
    """ OrderAdmin admin class """
    list_display = ['id', 'placed_at', 'customer']
