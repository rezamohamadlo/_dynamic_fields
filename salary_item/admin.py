from django.contrib import admin
from .models import SalaryItem
# Register your models here.
class SalaryItemAdmin(admin.ModelAdmin):
    list_display = [field.name for field in SalaryItem._meta.fields]
    search_fields = ['english_name', 'persian_name']

admin.site.register(SalaryItem, SalaryItemAdmin)