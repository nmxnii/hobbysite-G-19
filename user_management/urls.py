from django.urls import path
from .views import *

urlpatterns = [
    path('<int:pk>/', ProfileDetailView.as_view(), name='profile-detail'),
    path('<int:pk>/update', ProfileUpdateView.as_view(), name='profile-update'),
    path('create', ProfileCreateView.as_view(), name='profile-create'),
    # path('<int:pk>/create', ProfileCreateView.as_view(), name='profile-create'),
]

app_name = 'user_management'