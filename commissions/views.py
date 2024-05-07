from django.shortcuts import render
from django.views.generic.detail import DetailView
from django.views.generic import TemplateView, View
from django.views.generic.edit import CreateView, UpdateView
from django.views.generic.list import ListView
from django.http import HttpResponseRedirect
from .models import *
from .forms import *
from django.urls import reverse
# Create your views here.


class CommissionListView(ListView):
    model = Commission
    template_name = "commissions_list.html"


class CommissionDetailView(DetailView):
    model = Commission
    template_name = "commissions_detail.html"


class CommissionCreateView(View):
    # model = Commission
    # form_class = CommissionCreateForm
    template_name = "commissions_create.html"

    def get(self, request):
        commission_form = CommissionCreateForm()
        job_form = JobCreateForm()
        return render(request, 
        self.template_name, 
        {'commission_form': commission_form, 'job_form': job_form})
    
    def post(self, request, *args, **kwargs):
        commission_form=CommissionCreateForm(request.POST)
        job_form=JobCreateForm(request.POST)
        if commission_form.is_valid() and job_form.is_valid():
            commission = Commission()
            commission.title=commission_form.cleaned_data.get('title')
            commission.author=request.user.profile
            commission.description=commission_form.cleaned_data.get('description')
            commission.status=commission_form.cleaned_data.get('status')
            commission.save()
            job= Job()
            job.commission=commission
            job.status=job_form.cleaned_data.get('status')
            job.role=job_form.cleaned_data.get('role')
            job.manpower_required=job_form.cleaned_data.get('manpower_required')
            job.entry=job_form.cleaned_data.get('entry')
            job.save()
            return HttpResponseRedirect(reverse('commissions:commissions'))
            # return self.get(request, *args, **kwargs)
        else:
            Commission.object_list=Commission.get_queryset(**kwargs)
            Job.object_list=Job.get_queryset(**kwargs)
            
            context=self.get_context_data(**kwargs)
            context["commmission_form"]=commission_form
            context["job_form"] = job_form
            response = super().form_invalid(form)
            return self.render_to_response(context)



    def form_valid(self, form):
        # i think form_valid is for making
        # default values like pag nag exclude idk
        commission_form.instance.author = self.request.user.profile
        return super().form_valid(commission_form)

    def get_success_url(self):
        return reverse('commissions:commissions')
        # return reverse("commissions:commissions-detail", kwargs={"pk": (self.pk)})
    # def post(self,request, *args, **kwargs):
    #     form=CommissionCreateForm(request.POST)
    #     job_form= JobCreateForm(request.POST)
    #     if form.is_valid():
    #         commission = Commission()
    #         commission.title=form.cleaned_data.get('title')
    #         commission.author=request.user.profile
    #         commission.description=form.cleaned_data.get('description')
    #         commission.status=form.cleaned_data.get('status')
    #         commission.save()
    #         return self.get(request, *args, **kwargs)

    #     if job_form.is_valid():
    #         job= Job()
    #         job.commission=commission
    #         job.status=form.cleaned_data.get('job_status')
    #         job.role=form.cleaned_data.get('job_role')

    #         job.manpower_required=form.cleaned_data.get('manpower_required')
    #         job.entry=form.cleaned_data.get('entry')
    #         job.save()
    #         return self.get(request, *args, **kwargs)
    #     else:
    #         self.object_list=self.get_queryset(**kwargs)
    #         context=self.get_context_data(**kwargs)
    #         context["form"]=form
    #         response = super().form_invalid(form)
    #         return self.render_to_response(context)
# def job_create(request):
    # template_name='commissions_create.html'
    # commissions= Commission.objects.all()
    # jobs= Job.objects.all()

    # ctx={
    #     "commissions": commissions,
    #     "jobs": jobs,
    # }
    # if request.method == "POST":
    #     commission = Commission()
    #     commission.title = request.POST.get('title')
    #     commission.author = request.user.profile
    #     commission.description = request.POST.get('description')
    #     commission.status = request.POST.get('status')
    #     commission.save()
    #     job = Job()
    #     job.commission = commission
    #     job.status = request.POST.get('job_status')
    #     job.role = request.POST.get('job_role')
    #     job.manpower_required = request.POST.get('manpower_required')
    #     job.entry = request.POST.get('entry')
    #     job.save()
    #     # return render(request, 'commissions_create.html', ctx)
    #     return render(request, reverse("commissions:commissions-detail",
    #                             kwargs={"pk": (commission.pk)}), ctx)
    # else:
    #     return render(request, 'commissions_detail.html')
        # return render(request, reverse("commissions:commissions-detail",
        # kwargs={"pk": (commission.pk)}), ctx)

# class JobApplicationView(CreateView):
#     model=JobApplication
#     form_class=JobApplicationForm
#     template_name= "commissions_job_application.html"

#


class CommissionUpdateView(UpdateView):
    model = Commission
    form_class = CommissionUpdateForm
    template_name = "commissions_update.html"
