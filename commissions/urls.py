from django.urls import path
from .views import CommissionDetailView, CommissionListView

urlpatterns = [
    path('list/', CommissionListView.as_view(), name="commissions"),
    path('detail/<int:pk>', CommissionDetailView.as_view(),
         name='commissions-detail')
]

app_name = 'commissions'
