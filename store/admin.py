from django.contrib import admin
from . import models

admin.site.register(models.Collection)


# define the admin class
@admin.register(models.Product)
class ProductAdmin(admin.ModelAdmin):
    """ Product admin class """
    list_display = ['title', 'unit_price']
    list_editable = ['unit_price']
    list_per_page = 10

# this is the second way to define admin class
# admin.site.register(models.Product, ProductAdmin)


@admin.register(models.Customer)
class CustomerAdmin(admin.ModelAdmin):
    """ Customer admin class """
    list_display = ['first_name', 'last_name', 'membership']
    list_editable = ['membership']
    ordering = ['first_name', 'last_name']
    list_per_page = 10
