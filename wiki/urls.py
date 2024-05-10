from django.urls import path
from .views import *

urlpatterns = [
    path('articles/', WikiArticleView.as_view(), name='wiki_article_list'),
    path('article/<int:pk>', WikiDetailView.as_view(), name='wiki_article_detail'),
    path('article/add', WikiCreateView.as_view(), name='wiki_article_create'),
    path('article/<int:pk>/edit', WikiUpdateView.as_view(), name='wiki_article_update'),
    path('gallery/articles', ImageGalleryView.as_view(), name='wiki_gallery_view'),
]

app_name = 'wiki'
