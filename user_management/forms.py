from django import forms
from .models import *


class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = "__all__"
