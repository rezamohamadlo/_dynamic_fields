from django.db import models

# Create your models here.
class WorkingMonth(models.Model):
    id = models.SmallAutoField(primary_key=True)
    months = [
        ('01', 'فروردین'),
        ('02', 'اردیبهشت'),
        ('03', 'خرداد'),
        ('04', 'تیر'),
        ('05', 'مرداد'),
        ('06', 'شهریور'),
        ('07', 'مهر'),
        ('08', 'آبان'),
        ('09', 'آذر'),
        ('10', 'دی'),
        ('11', 'بهمن'),
        ('12', 'اسفند'),
    ]
    years = [(str(year), str(year)) for year in range(1396, 1405)]

    
    working_month_year = models.CharField(max_length=4, choices=years, blank=True, null=True, default=1404)
    working_month_name = models.CharField(max_length=2, choices=months, blank=True, null=True)
    working_month_and_year = models.CharField(max_length=6, editable=False, blank=True, null=True)


    def save(self, *args, **kwargs):
        self.working_month_and_year = f"{self.working_month_year}{self.working_month_name}"  
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.working_month_and_year}"

    class Meta:
        db_table = 'working_month'
        verbose_name = 'ماه کاری'
        verbose_name_plural = 'ماه های کاری'