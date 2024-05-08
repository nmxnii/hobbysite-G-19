from django.shortcuts import render, get_object_or_404
from django.views.generic.detail import DetailView
from django.views.generic import View
from django.views.generic.edit import CreateView, UpdateView
from django.views.generic.list import ListView
from django.forms import inlineformset_factory
from django.http import HttpResponseRedirect
from django.urls import reverse, reverse_lazy
from django.contrib import messages
from typing import Any
from django.http import HttpResponseRedirect
from .models import *
from .forms import *

# Create your views here.


class CommissionListView(ListView):
    model = Commission
    template_name = "commissions_list.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['jobs'] = Job.objects.all()
        context['applied'] = Commission.objects.filter()
        context['jobapplicant'] = JobApplication.objects.all()
        return context


class CommissionDetailView(DetailView):
    model = Commission
    template_name = "commissions_detail.html"

    def get_context_data(self, **kwargs) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        commission_pk = self.kwargs["pk"]
        context["commission"] = Commission.objects.get(pk=commission_pk)
        total_manpower = 0
        accepted_applicants = 0
        for job in Commission.objects.get(pk=commission_pk).jobs.all():
            for applicant in job.applicants.all():
                if applicant.status == 'accepted':
                    accepted_applicants += 1
        for job in Commission.objects.get(pk=commission_pk).jobs.all():
            total_manpower += job.manpower_required
        job_application_form = JobApplicationForm()
        context["total_manpower"] = total_manpower
        context["job_application_form"] = job_application_form
        context["open_manpower"] = total_manpower - accepted_applicants
        return context

    def post(self, request, pk):
        # ctx= self.get_context_data(**kwargs)
        job_application_form = JobApplicationForm(request.POST)
        if job_application_form.is_valid():
            print('if satisfy')
            job_application = JobApplication()
            job_application.job = Job.objects.get(
                pk=request.POST.get('job_pk'))
            job_application.applicant = request.user.profile
            job_application.status = 'pending'
            if not (job_application.job.applicants.all().filter(applicant=request.user.profile).exists()):
                job_application.save()
            commission = job_application.job.commission
        return HttpResponseRedirect(reverse('commissions:commissions-detail', kwargs={'pk': commission.pk}))


class CommissionCreateView(View):
    template_name = "commissions_create.html"

    def get(self, request):
        commission_form = CommissionCreateForm()
        # commission = Commission()
        JobFormSet = inlineformset_factory(
            Commission, Job, exclude=['commission'], extra=2)
        formset = JobFormSet()
        return render(request, self.template_name, {'commission_form': commission_form, 'formset': formset})

    def post(self, request, *args, **kwargs):
        commission_form = CommissionCreateForm(request.POST)
        JobFormSet = inlineformset_factory(
            Commission, Job, exclude=['commission'], extra=1)
        formset = JobFormSet(request.POST)
        if commission_form.is_valid():
            commission = Commission()
            commission_cd = commission_form.cleaned_data
            commission.title = commission_cd.get('title')
            commission.author = request.user.profile
            commission.description = commission_cd.get('description')
            commission.status = commission_cd.get('status')
            commission.save()
        else:
            messages.error(request, "ERROR. Form not submitted")
            return render(request, self.template_name, {'commission_form': commission_form, 'formset': formset})

        if formset.is_valid():
            for form in formset:
                job_form = form
                job = Job()
                cd = job_form.cleaned_data
                job.commission = commission
                job.role = cd.get('role')
                job.manpower_required = cd.get('manpower_required')
                job.status = cd.get('status')
                job.save()

        else:
            messages.error(request, "ERROR. Form not submitted")
            return render(request, self.template_name, {'commission_form': commission_form, 'formset': formset})

        commission_form = CommissionCreateForm()
        formset = JobFormSet()

        return HttpResponseRedirect(reverse('commissions:commissions'))


class CommissionUpdateView(UpdateView):
    model = Commission
    template_name = 'commissions_update.html'
    # Add all fields except 'created_on' and 'updated_on'
    fields = ['title', 'description', 'status']

    def get_context_data(self, **kwargs):
        JobFormSet = inlineformset_factory(
            Commission, Job, exclude=['commission'], extra=0)
        context = super().get_context_data(**kwargs)
        if self.request.POST:
            context['job_formset'] = JobFormSet(
                self.request.POST, instance=self.object)
        else:
            context['job_formset'] = JobFormSet(instance=self.object)
        return context

    def form_valid(self, form):
        context = self.get_context_data()
        job_formset = context['job_formset']
        print(job_formset.is_valid())
        if job_formset.is_valid():
            print('valid')
            self.object = form.save()
            job_formset.instance.commission = self.object
            job_formset.instance = self.object
            job_formset.save()

            if all(job.status == 'full' for job in self.object.jobs.all()):
                self.object.status = 'full'
            return HttpResponseRedirect(reverse('commissions:commissions'))
        else:
            print('not valid')
            print(job_formset.errors)
            return self.render_to_response(self.get_context_data(form=form, job_formset=job_formset))
