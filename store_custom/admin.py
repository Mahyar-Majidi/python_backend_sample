from django.contrib import admin
from django.contrib.contenttypes.admin import GenericTabularInline
from store.admin import ProductAdmin
from store.models import Product
from tags.models import TagItem
# Register your models here.


class TagInline(GenericTabularInline):
    """ Tag item inline show order """
    autocomplete_fields = ['tag']
    model = TagItem


class CustomProductAdmin(ProductAdmin):
    """ CustomProductAdmin class """
    inlines = [TagInline]


admin.site.unregister(Product)
admin.site.register(Product, CustomProductAdmin)
