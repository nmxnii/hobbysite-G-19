from django.views.generic.edit import UpdateView, CreateView
from django.views.generic.detail import DetailView
from django.views.generic import TemplateView, View
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from .models import Profile
from .forms import *
from django.contrib.auth.mixins import LoginRequiredMixin


class ProfileUpdateView(UpdateView):
    model = Profile
    form_class = ProfileUpdateForm
    template_name = 'profile_update.html'

    def get_success_url(self) -> str:
        return reverse_lazy("profile:profile-detail", kwargs={"pk": self.object.pk})


class ProfileDetailView(DetailView):
    model = Profile
    template_name = 'profile_detail.html'


class ProfileCreateView(CreateView):
    model = Profile
    form_class = ProfileCreateForm
    template_name = 'profile_create.html'
    
    def form_valid(self, form):
        if form.is_valid():
            profile=Profile()
            profile.user=self.request.user
            profile.display_name=form.cleaned_data.get('display_name')
            profile.email=form.cleaned_data.get('email')
            profile.user.user_id=form.cleaned_data.get('user_id')
            profile.save()
        return HttpResponseRedirect(reverse('home'))
    

    def get_success_url(self) -> str:
        return reverse('home')
