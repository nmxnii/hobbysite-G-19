from django.db import models
from django.urls import reverse

from user_management.models import Profile

class ArticleCategory(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()

    class Meta:
        ordering = ['name']
    
    def __str__(self):
        return self.name

class Article(models.Model):
    title = models.CharField(max_length=255)
    author = models.ForeignKey(Profile, on_delete=models.SET_NULL, null=True, blank=True)
    category = models.ForeignKey(ArticleCategory, on_delete=models.SET_NULL, null=True, blank=True)
    header_image = models.ImageField(upload_to='article_headers/', null=True, blank=True)
    entry = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_on']


    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse('blog:article_detail', args=str(self.pk))
    
    



    
