from django import forms

from .models import Article, Comment


class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        exclude = ['author'] 

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['author'].disabled=True

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['entry']