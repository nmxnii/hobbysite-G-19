from django.contrib import admin
from .models import Commission, Comment


class CommentInline(admin.TabularInline):
    model = Comment


class CommissionAdmin(admin.ModelAdmin):
    model = Commission
    list_display = ('title', 'description', 'people_required',
                    'created_on', 'updated_on')
    inlines = [CommentInline,]


admin.site.register(Commission, CommissionAdmin)
