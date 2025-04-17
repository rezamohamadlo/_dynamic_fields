from django.db import models
from salary_item.models import SalaryItem


class SalaryCalculation(models.Model):
    sum_of_items = models.IntegerField(default=0, editable=False)
    # other fields

    def update_total(self):
        self.sum_of_items = sum(item.amount for item in self.items.all())
        self.save()

class SalaryCalculationItem(models.Model):
    calculation = models.ForeignKey(SalaryCalculation, related_name='items', on_delete=models.CASCADE)
    salary_item = models.ForeignKey(SalaryItem, on_delete=models.CASCADE)
    amount = models.IntegerField(default=0)



