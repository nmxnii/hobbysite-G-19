from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.db.models import Max

from .models import Article, ArticleCategory


class BlogArticleView(ListView):
    model = Article
    template_name = "article_list.html"

    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)        
        context['article_category'] = ArticleCategory.objects.all()
        
        return context
    
class BlogDetailView(DetailView):
    model = Article
    template_name = "article_detail.html"