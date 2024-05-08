from django import forms
from .models import *


class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = "__all__"


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ["entry"]

class UpdateForm(forms.ModelForm):
    class Meta:
        model = Article
        exclude = ["author"]