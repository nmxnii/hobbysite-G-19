from django.db import models
from django.urls import reverse
from user_management.models import *


class ArticleCategory(models.Model):
    name = models.CharField(max_length=255, help_text="Enter Category Title")
    description = models.TextField(help_text="Enter Category Description")

    class Meta:
        ordering = ['name']
        verbose_name_plural = "Article Categories"

    def __str__(self):
        return self.name


class Article(models.Model):
    title = models.CharField(max_length=255, help_text="Enter Article Title")
    author = models.ForeignKey(
        Profile, on_delete=models.SET_NULL, null=True, blank=True, related_name='author')
    category = models.ForeignKey(
        ArticleCategory, on_delete=models.SET_NULL, null=True, blank=True)
    entry = models.TextField(help_text="Enter Article Descrption")
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    article_image = models.ImageField(upload_to="images/", null=True,)

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('wiki:wiki_article_detail', kwargs={'pk': (self.pk)})


class Comment(models.Model):
    author = models.ForeignKey(
        Profile, on_delete=models.SET_NULL, null=True, blank=True)
    article = models.ForeignKey(
        Article, on_delete=models.CASCADE)
    entry = models.TextField(help_text="Enter Article Comment")
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['created_on']
