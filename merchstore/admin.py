from django.contrib import admin

from .models import ProductType, Product


class ProductAdmin(admin.ModelAdmin):
    model=Product
    list_display = ['name']


class ProductTypeAdmin(admin.ModelAdmin): 
    model = ProductType 
    list_display = ['name']


admin.site.register(ProductType, ProductTypeAdmin) 
admin.site.register(Product, ProductAdmin) 
# Register your models here.
