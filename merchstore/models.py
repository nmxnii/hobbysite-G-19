from django.urls import reverse
from django.db import models

from user_management.models import Profile


class ProductType(models.Model): 
    name = models.CharField(max_length=255) 
    description = models.TextField()

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name


class Product(models.Model): 
    name=models.CharField(max_length=255)
    ProductType=models.ForeignKey(
        ProductType, 
        on_delete=models.SET_NULL, 
        related_name='product', 
        null=True
    )
    Owner=models.ForeignKey(
        Profile,
        on_delete=models.CASCADE,
        related_name='product'
    )
    description=models.TextField()
    price=models.DecimalField(max_digits=100, decimal_places=2)
    stock=models.IntegerField(blank=True, null=True)
    statusOptions=(
        ('Available','Available'),
        ('On Sale','On Sale'),
        ('Out of Stock', 'Out of Stock')
    )
    status=models.CharField(max_length=25, choices=statusOptions, default='Available')

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name    
    
    def get_absolute_url(self):
        return reverse('merchstore:product_detail', args=[self.pk])


class transaction(models.Model):
    buyer=models.ForeignKey(
        Profile,
        on_delete=models.SET_NULL, 
        related_name='buyer', 
        null=True
    )
    product=models.ForeignKey(
        Product,
        on_delete=models.SET_NULL, 
        related_name='product', 
        null=True
    )
    amount=models.PositiveIntegerField(blank=True, null=True)
    statusTOptions=(
        ('On cart','On cart'),
        ('To Pay', 'To Pay'),
        ('To Ship', 'To Ship'),
        ('To Receive', 'To Receive'),
        ('Delivered', 'Delivered')
    )
    status=models.CharField(max_length=25, choices=statusTOptions, default=False)
    createdOn=models.DateTimeField(auto_now_add=True)
    class Meta:
        ordering = ['-createdOn']




# Create your models here.
