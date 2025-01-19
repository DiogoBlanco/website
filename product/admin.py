from django.contrib import admin
from .models import Product


class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'active', 'price')
    search_fields = ('name',)
    list_filter = ('active',)


admin.site.register(Product, ProductAdmin)
