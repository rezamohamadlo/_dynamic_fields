from django.contrib import admin
from .models import SalaryTaxCalculation
# Register your models here.
class SalaryTaxCalculationAdmin(admin.ModelAdmin):
    list_display = [field.name for field in SalaryTaxCalculation._meta.fields]
    search_fields = ['english_name', 'persian_name']

admin.site.register(SalaryTaxCalculation, SalaryTaxCalculationAdmin)