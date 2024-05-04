from django.urls import path


from .views import BlogArticleView, BlogDetailView, ArticleCreateView, ArticleUpdateView

urlpatterns = [
    path('articles/', BlogArticleView.as_view(), name='article_list'),
    path('article/<int:pk>', BlogDetailView.as_view(), name='article_detail'),
    path('article/add', ArticleCreateView.as_view(), name='article_create'),
    path('article/<int:pk>/edit', ArticleUpdateView.as_view(), name='article_update'),

]

app_name = 'blog'