from django.db import models
from salary_item.models import SalaryItem


class SalaryCalculation(models.Model):
    tax = models.IntegerField(default=0, editable=False)
    # other fields

    def update_total(self):
        total = self.items.filter(salary_item__include_in_tax=True).aggregate(
            total_amount=models.Sum('amount')
        )['total_amount'] or 0
        self.tax = total
        self.save()

class SalaryCalculationItem(models.Model):
    calculation = models.ForeignKey(SalaryCalculation, related_name='items', on_delete=models.CASCADE)
    salary_item = models.ForeignKey(SalaryItem, on_delete=models.CASCADE)
    amount = models.IntegerField(default=0)



