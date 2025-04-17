from django.contrib import admin
from .models import Employee  # Replace .models with the actual path to your Employee model

class EmployeeAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Employee._meta.fields]
    search_fields = [field.name for field in Employee._meta.fields]
    ordering = [field.name for field in Employee._meta.fields]
    list_filter = [field.name for field in Employee._meta.fields]
admin.site.register(Employee, EmployeeAdmin)
