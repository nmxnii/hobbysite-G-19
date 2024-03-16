from django.contrib import admin

from .models import Article, ArticleCategory

class ArticleCategoryInLine(admin.TabularInline):
    model = ArticleCategory

class ArticleAdmin(admin.ModelAdmin):
    inlines = [ArticleCategoryInLine]

admin.site.register(Article, ArticleAdmin)
