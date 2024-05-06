from django.shortcuts import redirect
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView
from django.views.generic.edit import UpdateView

from django.urls import reverse_lazy


from .forms import ArticleForm, CommentForm
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

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        article = self.get_object()
        context['comment_form'] = CommentForm() 
        context['comments'] = article.comment_set.all()  # Get all comments for the article
        return context

    def post(self, request, *args, **kwargs):
        article = self.get_object()
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            new_comment.author = request.user.profile
            new_comment.article = article
            new_comment.save()
            return redirect('blog:article_detail', pk=article.pk)
        else:
            return self.render_to_response(self.get_context_data(comment_form=comment_form))

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
    form_class = ArticleForm
    template_name = "article_update.html"

    def get_success_url(self):
        return reverse_lazy("blog:article_detail", kwargs={'pk': self.object.pk})

    def form_valid(self, form):
        form.instance.author = self.request.user.profile
        return super().form_valid(form)

class ImageGalleryView(ListView):
    model = Article
    template_name = "blog_gallery_view.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['articles'] = Article.objects.all() 
        return context
