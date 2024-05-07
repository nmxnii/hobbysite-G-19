from django import forms
from .models import *

class CommissionCreateForm(forms.ModelForm):
     class Meta:
          model = Commission
          # fields='_all_'
          exclude=['author']      
          #     
     

class CommissionUpdateForm(forms.ModelForm):
     class Meta:
          model = Commission
          exclude=['author']
     
class JobCreateForm(CommissionCreateForm,forms.ModelForm):
     class Meta:
          model = Job
          fields='__all__'
          exclude=['commission']

class JobApplicationForm(forms.ModelForm):
     class Meta:
          model=JobApplication
          fields='__all__'
          exclude=['status']