from django.db import models
from django.urls import reverse

class Article(models.Model):
    title = models.CharField(max_length=255)
    category = models.ForeignKey(ArticleCategory, on_delete=models.SET_NULL, null=True)
    entry = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created on']


    def __str__(self):
        return self.name
    

class ArticleCategory(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()

    def get_absolute_url(self):
        return reverse("model_detail", kwargs={"pk": self.pk})


    
