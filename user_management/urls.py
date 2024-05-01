from django.urls import path
from .views import *

urlpatterns = [
    path('<int:pk>/', ProfileDetailView.as_view(), name='profile-detail'),
    path('<int:pk>/update', ProfileUpdateView.as_view(), name='profile-update'),
]

app_name = 'user_management'