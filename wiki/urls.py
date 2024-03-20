from django.urls import path
from .views import WikiArticleView, WikiDetailView

urlpatterns = [
    path('articles/', WikiArticleView.as_view(), name='wiki_article_list'),
    path('article/<int:pk>', WikiDetailView.as_view(), name='wiki_article_detail')
]

app_name = 'wiki'
