from django.shortcuts import render
from django.http import HttpResponseRedirect
from user_management.models import Profile
from django.urls import reverse
def home(request):
    return render(request, "home.html")
