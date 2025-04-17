from django.db import models

# Create your models here.
from django.db import models


class SalaryItem(models.Model):
    id = models.SmallAutoField(primary_key=True)
    english_name = models.CharField(max_length=50, verbose_name='نام انگلیسی')
    persian_name = models.CharField(max_length=50, verbose_name='نام فارسی')
    include_in_base_wage = models.BooleanField(default= False, verbose_name='درج در حقوق مبنا')
    include_in_insurance = models.BooleanField(default= False, verbose_name='شامل بیمه')
    include_in_tax = models.BooleanField(default= False, verbose_name='شامل مالیات')
    include_in_overtime = models.BooleanField(default=False, verbose_name='شامل اضافه کاری')
    
    def __str__(self):
        return self.persian_name
    
    class Meta:
        db_table = 'salary_item'
        verbose_name = 'ایتم حقوقی'
        verbose_name_plural = 'ایتم های حقوقی'