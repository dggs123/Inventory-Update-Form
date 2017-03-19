from django.contrib import admin
from .models import Product

# Register your models here.
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'product_type', 'price', 'quantity']
    list_filter = ['product_type']

admin.site.register(Product, ProductAdmin)