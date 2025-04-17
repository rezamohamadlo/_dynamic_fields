from django.contrib import admin
from .models import SalaryTaxThreshold


class SalaryTaxThresholdAdmin(admin.ModelAdmin):
    list_display = [field.name for field in SalaryTaxThreshold._meta.fields]
    search_fields = [field.name for field in SalaryTaxThreshold._meta.fields]
    ordering = [field.name for field in SalaryTaxThreshold._meta.fields]
    list_filter = [field.name for field in SalaryTaxThreshold._meta.fields]

# Registering the Organization model with the custom admin class
admin.site.register(SalaryTaxThreshold, SalaryTaxThresholdAdmin)