from django.contrib import admin
from .models import SalaryItem
# Register your models here.
class SalaryItemAdmin(admin.ModelAdmin):
    list_display= ('english_name', 'persian_name', 'include_in_base_wage', 'include_in_insurance', 'include_in_tax')
    search_fields = ['english_name', 'persian_name']

admin.site.register(SalaryItem, SalaryItemAdmin)