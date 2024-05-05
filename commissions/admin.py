from django.contrib import admin
from .models import Commission, Job


class JobInline(admin.TabularInline):
    model = Job


class CommissionAdmin(admin.ModelAdmin):
    model = Commission
    list_display = ('title', 'description','created_on', 'updated_on')
    inlines = [JobInline,]


admin.site.register(Commission, CommissionAdmin)

