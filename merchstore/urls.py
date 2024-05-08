from django.urls import path

from .views import ProductListView, ProductDetailView, ProductCreateView, ProductUpdateView,TransactionListView,CartView

urlpatterns = [
path('items/', ProductListView.as_view(), name='product_list'),
path('item/<int:pk>', ProductDetailView.as_view(), name='product_detail'),
path('item/add', ProductCreateView.as_view(), name='product_create'),
path('item/<int:pk>/edit', ProductUpdateView.as_view(), name='product_update'),
path('transactions', TransactionListView.as_view(), name='product_transaction_list'),
path('cart', CartView.as_view(), name='product_cart_view')
]
app_name = 'merchstore'