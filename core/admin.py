from django.contrib import admin
from django.contrib.contenttypes.admin import GenericTabularInline
from .models import User
from store.admin import ProductAdmin
from store.models import Product
from tags.models import TagItem
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
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


@admin.register(User)
class UserAdmin(BaseUserAdmin):
    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": ("username", "password1", "password2", "email", "first_name", "last_name"),
            },
        ),
    )
