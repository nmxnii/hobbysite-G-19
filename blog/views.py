from django.views.generic.detail import DetailView
from django.views.generic.list import ListView

from .models import Article


class BlogArticleView(ListView):
    model = Article
    template_name = "blog_article.html"

class BlogDetailView(DetailView):
    model = Article
    template_name = "blog_detail.html"