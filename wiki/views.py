
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView
from .models import *
from .forms import *


class WikiArticleView(ListView):
    model = Article
    template_name = "wiki_article_list.html"

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx["categories"] = ArticleCategory.objects.all()
        return ctx


class WikiDetailView(DetailView):
    model = Article
    template_name = "wiki_article_detail.html"

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx["object_list"] = Article.objects.all()
        article = self.get_object()
        ctx["comment_form"] = CommentForm()
        ctx["comments"] = article.comment_set.all()
        return ctx

    def post(self, request, *args, **kwargs):
        article = self.get_object()
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            new_comment.author = request.user.profile
            new_comment.article = article
            new_comment.save()
            return redirect('wiki:wiki_article_detail', pk=article.pk)
        else:
            return self.render_to_response(self.get_context_data(comment_form=comment_form))


class WikiCreateView(CreateView):
    model = Article
    template_name = "wiki_article_create.html"
    form_class = ArticleForm

    def get_success_url(self):
        return reverse_lazy("wiki:wiki_article_list")
    
    def get_initial(self):
        initial = super().get_initial()
        initial['author'] = self.request.user.profile
        return initial
    
    def get_form(self, form_class=None):
        form = super().get_form(form_class)
        form.fields['author'].widget.attrs['disabled'] = True
        return form

    def form_valid(self, form):
        form.instance.author = self.request.user.profile
        return super().form_valid(form)


class WikiUpdateView(UpdateView):
    model = Article
    template_name = "wiki_article_update.html"
    form_class = UpdateForm

    def get_success_url(self):
        return reverse_lazy("wiki:wiki_article_list")

    def form_valid(self, form):
        form.instance.author = self.request.user.profile
        return super().form_valid(form)


class ImageGalleryView(ListView):
    model = Article
    template_name = "wiki_gallery_view.html"