from django.contrib import admin
from .models import WorkingMonth  # Ensure this import is correct

class WorkingMonthAdmin(admin.ModelAdmin):
    list_display = ('working_month_and_year', )
    # list_display = [field.name for field in WorkingMonth._meta.fields]
    search_fields = [field.name for field in WorkingMonth._meta.fields]
    ordering = [field.name for field in WorkingMonth._meta.fields]
    list_filter = [field.name for field in WorkingMonth._meta.fields]

admin.site.register(WorkingMonth, WorkingMonthAdmin)