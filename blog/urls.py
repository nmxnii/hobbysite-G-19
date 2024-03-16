from django.urls import path


from .views import BlogArticleView, BlogDetailView

urlpatterns = [
    path('blogs/article/', BlogArticleView.as_view(), name='article'),
    path('blog/article/1', BlogDetailView.as_view(), name=
         'blog_detail')
]