from django.contrib import admin
from .models import *


class JobInline(admin.TabularInline):
    model = Job

class JobApplicationInline(admin.TabularInline):
    model=JobApplication

class CommissionAdmin(admin.ModelAdmin):
    model = Commission
    list_display = ('title', 'description','created_on', 'updated_on')
    inlines = [JobInline,]

class JobAdmin(admin.ModelAdmin):
    model=Job
    list_display=('status', 'manpower_required', 'role')
    inlines=[JobApplicationInline,]

class JobApplicationAdmin(admin.ModelAdmin):
    model=JobApplication

admin.site.register(Commission, CommissionAdmin)
admin.site.register(Job,JobAdmin)
admin.site.register(JobApplication, JobApplicationAdmin)
