from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from .models import Article


class WikiArticleView(ListView):
    model = Article
    template_name = "wiki_article_list.html"


class WikiDetailView(DetailView):
    model = Article
    template_name = "wiki_article_detail.html"
