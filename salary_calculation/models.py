from django.db import models
from salary_item.models import SalaryItem
from employee.models import Employee
from working_month.models import WorkingMonth
from salary_tax_calculation.models import SalaryTaxCalculation
from employee_workload.models import EmployeeWorkload

class SalaryCalculation(models.Model):
    employee = models.ForeignKey(Employee, blank=True, null=True, on_delete=models.PROTECT, verbose_name='کارمند')
    working_month = models.ForeignKey(WorkingMonth, blank=True, null=True, on_delete=models.PROTECT, verbose_name='ماه کاری')
    employee_workload = models.ForeignKey(EmployeeWorkload, blank=True, null=True,editable=False, on_delete=models.PROTECT, verbose_name='کارکرد کارمند')
    tax = models.IntegerField(default=0, editable=False, verbose_name='مالیات')
    insurance = models.IntegerField(default=0, editable=False, verbose_name='مجموع شامل بیمه')
    insurance_employee_share = models.IntegerField(default=0, editable=False, verbose_name='ییمه سهم کارگر')
    insurance_employer_share = models.IntegerField(default=0, editable=False, verbose_name='ییمه سهم کارفرما')
    base_wage = models.IntegerField(default=0, editable=False, verbose_name='حقوق مبنا')
    overtime = models.IntegerField(default=0, editable=False, verbose_name='اضافه کار')

    # other fields

    def update_total(self):
        #determine employee workload
        if self.employee and self.working_month:
            try:
                # Get the matching EmployeeWorkload
                workload = EmployeeWorkload.objects.get(
                    employee=self.employee,
                    employee_workload_working_month=self.working_month
                )
                self.employee_workload = workload
            except EmployeeWorkload.DoesNotExist:
                # Handle case where no matching workload exists
                self.employee_workload = None
                # You might want to log this or raise an exception
                # depending on your requirements
        
        #calculate tax
        total_salary = self.items.filter(salary_item__include_in_tax=True).aggregate(
            total=models.Sum('amount')
        )['total'] or 0

        tax_calculation, created = SalaryTaxCalculation.objects.get_or_create(
            salary_tax_calculation_employee=self.employee,
            salary_tax_calculation_working_month=self.working_month,
            defaults={'salary_tax_calculation_salary': total_salary}
        )
        
        if not created:
            tax_calculation.salary_tax_calculation_salary = total_salary
            tax_calculation.save()
        
        self.tax = tax_calculation.salary_tax_calculation_calculated_tax or 0

        #calculate insurance
        self.insurance = self.items.filter(salary_item__include_in_insurance=True).aggregate(
            total=models.Sum('amount')
        )['total'] or 0
        self.insurance_employee_share = self.insurance * 0.07
        self.insurance_employer_share = self.insurance * 0.23   
        
        #calculate overtime
        overtime_rate = self.items.filter(salary_item__include_in_overtime=True).aggregate(
            total=models.Sum('amount')
        )['total'] or 0
        self.overtime = overtime_rate * self.employee_workload.employee_workload_overtime_hours

        #calculate base_wage
        base_wage_rate = self.items.filter(salary_item__include_in_base_wage=True).aggregate(
            total=models.Sum('amount')
        )['total'] or 0
        self.base_wage = base_wage_rate * self.employee_workload.employee_workload_work_days
        self.save()

    class Meta:
        db_table = 'salary_calculation'
        verbose_name = 'محاسبه حقوق'
        verbose_name_plural = 'محاسبه حقوق ها'



class SalaryCalculationItem(models.Model):
    calculation = models.ForeignKey(SalaryCalculation, related_name='items', on_delete=models.CASCADE)
    salary_item = models.ForeignKey(SalaryItem, on_delete=models.CASCADE)
    amount = models.IntegerField(default=0)



