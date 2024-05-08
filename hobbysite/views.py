from django.shortcuts import render
from django.http import HttpResponseRedirect
from user_management.models import Profile
from django.urls import reverse
def home(request):
    if not (Profile.objects.filter(pk=request.user.pk).exists()) :
        return HttpResponseRedirect(reverse('profile:profile-create', kwargs={"pk": request.user.pk}))

    return render(request, "home.html")
