from django.contrib import admin
from .models import SalaryCalculation, SalaryCalculationItem

class SalaryCalculationItemInline(admin.TabularInline):
    model = SalaryCalculationItem
    extra = 0  # No extra empty forms by default
    autocomplete_fields = ['salary_item']  # Optional, for easier selection if many items

# Register your models here.
class SalaryCalculationAdmin(admin.ModelAdmin):
    list_display = [field.name for field in SalaryCalculation._meta.fields]
    inlines = [SalaryCalculationItemInline]
    readonly_fields = ('tax', 'insurance')  # Make total read-only if you want

    def save_related(self, request, form, formsets, change):
        super().save_related(request, form, formsets, change)
        form.instance.update_total()  # Recalculate tax after saving related items


admin.site.register(SalaryCalculation, SalaryCalculationAdmin)