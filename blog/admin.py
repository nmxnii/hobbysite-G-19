from django.contrib import admin

from .models import Article, ArticleCategory


class ArticleCategoryInLine(admin.TabularInline):
    model = ArticleCategory
    

class Article(admin.ModelAdmin):
    model = Article
    inlines = [ArticleCategoryInLine]

    
admin.site.register(Article, ArticleAdmin)