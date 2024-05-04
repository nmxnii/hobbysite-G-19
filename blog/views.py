from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView
from django.views.generic.edit import UpdateView

from django.urls import reverse_lazy


from .forms import ArticleForm, ArticleUpdateForm
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

class ArticleCreateView(CreateView):
    model = Article
    form_class = ArticleForm
    template_name = "article_create.html"

    def get_success_url(self):
        return reverse_lazy("blog:article_list")

    def form_valid(self, form):
        form.instance.author = self.request.user.profile
        return super().form_valid(form)

class ArticleUpdateView(UpdateView):
    model = Article
    form_class = ArticleUpdateForm
    template_name = "article_update.html"

    def get_success_url(self):
        return reverse_lazy("blog:article_detail", kwargs={'pk': self.object.pk})

    def form_valid(self, form):
        form.instance.author = self.request.user.profile
        return super().form_valid(form)
    
