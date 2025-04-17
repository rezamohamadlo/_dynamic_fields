from django.db import models
from salary_tax_threshold.models import SalaryTaxThreshold  # Replace with your app name
from decimal import Decimal
from employee.models import Employee
from working_month.models import WorkingMonth

class SalaryTaxCalculation(models.Model):
    id = models.BigAutoField(primary_key=True)
    salary_tax_calculation_employee = models.ForeignKey(Employee, on_delete=models.PROTECT, blank=True, null=True, verbose_name='کارمند')
    salary_tax_calculation_working_month = models.ForeignKey(WorkingMonth, blank=True, null=True, on_delete=models.PROTECT, verbose_name='ماه کاری')
    salary_tax_calculation_salary = models.DecimalField(max_digits=16, decimal_places=0, verbose_name='حقوق')
    salary_tax_calculation_calculated_tax = models.DecimalField(default=0, max_digits=16, decimal_places=0, verbose_name='مالیات محاسبه شده', null=True, blank=True, editable=False)


    def save(self, *args, **kwargs):
        thresholds = []
        percentages = []

        for item in SalaryTaxThreshold.objects.order_by('salary_tax_threshold_amount'):
            thresholds.append(item.salary_tax_threshold_amount)
            percentages.append(item.salary_tax_threshold_percentage)

        tax = Decimal(0)
        remaining_salary = self.salary_tax_calculation_salary
        break_outer_loop = False

        for i in range(len(thresholds) - 1, -1, -1):
            if break_outer_loop:
                 break
            if remaining_salary > thresholds[i]:
                for j in range(i, -1, -1):
                    tax += (remaining_salary - thresholds[j]) * percentages[j] / 100

                    if j == 0:
                        break_outer_loop = True
                    break
                else:
                    remaining_salary = thresholds[j] 
                if break_outer_loop:
                    break
                else:
                    remaining_salary = thresholds[j] 
                if break_outer_loop:
                    break

        self.salary_tax_calculation_calculated_tax = tax
        super().save(*args, **kwargs)


    def __str__(self):
        return f"Salary: {self.salary_tax_calculation_salary}, Tax: {self.salary_tax_calculation_calculated_tax}"
    