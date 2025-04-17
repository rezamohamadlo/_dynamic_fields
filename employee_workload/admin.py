from django.contrib import admin
from .models import EmployeeWorkload

class EmployeeWorkloadAdmin(admin.ModelAdmin):
    list_display = [field.name for field in EmployeeWorkload._meta.fields]
    search_fields = [field.name for field in EmployeeWorkload._meta.fields]
    ordering = [field.name for field in EmployeeWorkload._meta.fields]
    list_filter = [field.name for field in EmployeeWorkload._meta.fields]

admin.site.register(EmployeeWorkload, EmployeeWorkloadAdmin)