from django.db import models
from salary_item.models import SalaryItem


class SalaryCalculation(models.Model):
    tax = models.IntegerField(default=0, editable=False, verbose_name='مالیات')
    insurance = models.IntegerField(default=0, editable=False, verbose_name='بیمه')
    base_wage = models.IntegerField(default=0, editable=False, verbose_name='حقوق مبنا')
    overtime = models.IntegerField(default=0, editable=False, verbose_name='اضافه کار')
    # other fields

    def update_total(self):
        self.tax = self.items.filter(salary_item__include_in_tax=True).aggregate(
            total=models.Sum('amount')
        )['total'] or 0

        self.insurance = self.items.filter(salary_item__include_in_insurance=True).aggregate(
            total=models.Sum('amount')
        )['total'] or 0

        self.base_wage = self.items.filter(salary_item__include_in_base_wage=True).aggregate(
            total=models.Sum('amount')
        )['total'] or 0

        self.overtime = self.items.filter(salary_item__include_in_overtime=True).aggregate(
            total=models.Sum('amount')
        )['total'] or 0

        self.save()

class SalaryCalculationItem(models.Model):
    calculation = models.ForeignKey(SalaryCalculation, related_name='items', on_delete=models.CASCADE)
    salary_item = models.ForeignKey(SalaryItem, on_delete=models.CASCADE)
    amount = models.IntegerField(default=0)



