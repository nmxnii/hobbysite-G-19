from django.urls import path


from .views import BlogArticleView, BlogDetailView

urlpatterns = [
    path('blog/articles/', BlogArticleView.as_view(), name='article'),
    path('blog/article/<int:pk>', BlogDetailView.as_view(), name=
         'blog_detail')
]

app_name = 'blog'