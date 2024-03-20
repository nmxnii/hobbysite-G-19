from django.shortcuts import render
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from .models import Commission


# Create your views here.
class CommissionListView(ListView):
    model = Commission
    template_name = "commissions_list.html"


class CommissionDetailView(DetailView):
    model = Commission
    template_name = "commissions_detail.html"
