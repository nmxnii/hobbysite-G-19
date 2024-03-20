from django.urls import reverse
from django.db import models


class ProductType(models.Model): 
    name = models.CharField(max_length=255) #this is kinda redundant bcs the max chara length is 255 so how
    description = models.TextField()

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name


class Product(models.Model): 
    name = models.CharField(max_length=255)
    ProductType = models.ForeignKey(
        ProductType, 
        on_delete=models.SET_NULL, 
        related_name='product', 
        null=True
    )
    description = models.TextField()
    price = models.DecimalField(max_digits=100, decimal_places=2)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name    
    
    def get_absolute_url(self):
        return reverse('merchstore:product_detail', args=[self.pk])





# Create your models here.
