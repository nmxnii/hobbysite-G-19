from django.urls import path


from .views import BlogArticleView, BlogDetailView

urlpatterns = [
    path('articles/', BlogArticleView.as_view(), name='article_list'),
    path('article/<int:pk>', BlogDetailView.as_view(), name='article_detail')
]

app_name = 'blog'