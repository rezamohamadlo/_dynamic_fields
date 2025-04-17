from django.db import models
from salary_item.models import SalaryItem
from employee.models import Employee
from working_month.models import WorkingMonth
from salary_tax_calculation.models import SalaryTaxCalculation

class SalaryCalculation(models.Model):
    employee = models.ForeignKey(Employee, blank=True, null=True, on_delete=models.PROTECT, verbose_name='کارمند')
    working_month = models.ForeignKey(WorkingMonth, blank=True, null=True, on_delete=models.PROTECT, verbose_name='ماه کاری')
    tax = models.IntegerField(default=0, editable=False, verbose_name='مالیات')
    insurance = models.IntegerField(default=0, editable=False, verbose_name='بیمه')
    base_wage = models.IntegerField(default=0, editable=False, verbose_name='حقوق مبنا')
    overtime = models.IntegerField(default=0, editable=False, verbose_name='اضافه کار')
    # other fields

    def update_total(self):
        total_salary = self.items.filter(salary_item__include_in_tax=True).aggregate(
            total=models.Sum('amount')
        )['total'] or 0

        # Get or create SalaryTaxCalculation for this employee and working month
        tax_calculation, created = SalaryTaxCalculation.objects.get_or_create(
            salary_tax_calculation_employee=self.employee,
            salary_tax_calculation_working_month=self.working_month,
            defaults={'salary_tax_calculation_salary': total_salary}
        )
        
        # If it already existed, update the salary and save to trigger tax calculation
        if not created:
            tax_calculation.salary_tax_calculation_salary = total_salary
            tax_calculation.save()
        
        self.tax = tax_calculation.salary_tax_calculation_calculated_tax or 0

        #calculate insurance
        self.insurance = self.items.filter(salary_item__include_in_insurance=True).aggregate(
            total=models.Sum('amount')
        )['total'] or 0

        #calculate base_wage
        self.base_wage = self.items.filter(salary_item__include_in_base_wage=True).aggregate(
            total=models.Sum('amount')
        )['total'] or 0

        #calculate overtime
        self.overtime = self.items.filter(salary_item__include_in_overtime=True).aggregate(
            total=models.Sum('amount')
        )['total'] or 0

        self.save()

class SalaryCalculationItem(models.Model):
    calculation = models.ForeignKey(SalaryCalculation, related_name='items', on_delete=models.CASCADE)
    salary_item = models.ForeignKey(SalaryItem, on_delete=models.CASCADE)
    amount = models.IntegerField(default=0)



