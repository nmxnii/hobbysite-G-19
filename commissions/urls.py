from django.urls import path
from .views import *

urlpatterns = [
    path('list/', CommissionListView.as_view(), name="commissions"),
    path('detail/<int:pk>', CommissionDetailView.as_view(), name='commissions-detail'),
    path('add/', CommissionCreateView.as_view(), name='commissions-create'),
    path('<int:pk>/edit/', CommissionUpdateView.as_view(), name='commissions-update'),
]

app_name = 'commissions'
