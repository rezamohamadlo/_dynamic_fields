from django.db import models

class SalaryTaxThreshold(models.Model):
    id = models.AutoField(primary_key=True)
    salary_tax_threshold_amount = models.DecimalField(default=0,  max_digits=16, decimal_places=0, verbose_name='مبلغ مبنا')
    salary_tax_threshold_percentage = models.DecimalField(default=0, max_digits=5, decimal_places=2, verbose_name='درصد')
    salary_tax_threshold_base_year = models.DateField(default='1403-01-01', verbose_name='سال پایه')
    class Meta:
            db_table = 'salary_tax_threshold'  

    