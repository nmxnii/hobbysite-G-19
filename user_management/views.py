from django.views.generic.edit import UpdateView
from django.views.generic.detail import DetailView
from django.urls import reverse_lazy
from .models import Profile
from .forms import *
from django.contrib.auth.mixins import LoginRequiredMixin



class ProfileUpdateView(LoginRequiredMixin,UpdateView):
    model = Profile
    form_class= ProfileUpdateForm
    template_name= 'profile_update.html'
    
    def get_success_url(self) -> str:
        return reverse_lazy("profile:profile-detail", kwargs={"pk": self.object.pk})

class ProfileDetailView(LoginRequiredMixin,DetailView):
    model=Profile
    template_name='profile_detail.html'
    
    

# Create your views here.