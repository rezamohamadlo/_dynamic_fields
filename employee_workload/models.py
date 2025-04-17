from django.db import models
from employee.models import Employee
from working_month.models import WorkingMonth   

class EmployeeWorkload(models.Model):
    id = models.AutoField(primary_key=True, verbose_name='شناسه') 
    employee = models.ForeignKey(Employee, blank=True, null=True, on_delete=models.PROTECT, verbose_name='کارمند')  
    # employee_workload_working_month = models.CharField(max_length=15, blank=True, null=True, verbose_name='ماه کاری')
    employee_workload_working_month = models.ForeignKey(WorkingMonth,on_delete=models.DO_NOTHING, blank=True, null=True, verbose_name='ماه کاری')
    employee_workload_first_name = models.CharField(max_length=50, blank=True, null=True, editable=False, verbose_name='نام')  
    employee_workload_last_name = models.CharField(max_length=50, blank=True, null=True, editable=False, verbose_name='نام خانوادگی')  
    employee_workload_national_code = models.CharField(max_length=10, blank=True, null=True, editable=False, verbose_name='کد ملی')  
    employee_workload_personnel_code = models.CharField(max_length=50, blank=True, null=True, editable=False, verbose_name='کد پرسنلی')  
    employee_workload_work_days = models.SmallIntegerField(blank=True, null=True, verbose_name='کارکرد (روز)')  
    # employee_workload_absence_days = models.SmallIntegerField(blank=True, null=True, verbose_name='غیبت (روز)')  
    # employee_workload_sick_leave_days = models.SmallIntegerField(blank=True, null=True, verbose_name='مرخصی استعلاجی (روز)')  
    # employee_workload_unpaid_leave_days = models.SmallIntegerField(blank=True, null=True, verbose_name='مرخصی بدون حقوق (روز)')  
    # employee_workload_earned_leave_days = models.SmallIntegerField(blank=True, null=True, verbose_name='مرخصی استحقاقی (روز)')  
    # employee_workload_mission_days = models.SmallIntegerField(blank=True, null=True, verbose_name='ماموریت (روز)')  
    # employee_workload_shift_22_5_days = models.SmallIntegerField(blank=True, null=True, verbose_name='نوبت کاری 22.5% (روز)')  
    # employee_workload_shift_15_days = models.SmallIntegerField(blank=True, null=True, verbose_name='نوبت کاری 15% (روز)')  
    # employee_workload_shift_10_days = models.SmallIntegerField(blank=True, null=True, verbose_name='نوبت کاری 10% (روز)')  
    # employee_workload_commuting_cost = models.IntegerField(blank=True, null=True, verbose_name='هزینه ایاب و ذهاب (ریال)')  
    # employee_workload_production_increase_bonus = models.BigIntegerField(blank=True, null=True, verbose_name='پاداش افزایش تولید (ریال)')  
    # employee_workload_mission_cost = models.BigIntegerField(blank=True, null=True, verbose_name='هزینه های ماموریت (ریال)')  
    # employee_workload_food_cost = models.BigIntegerField(blank=True, null=True, verbose_name='هزینه غذای مصرفی (ریال)')  
    # employee_workload_other_deductions = models.BigIntegerField(blank=True, null=True, verbose_name='سایر کسورات (ریال)')  
    employee_workload_overtime_hours = models.SmallIntegerField(blank=True, null=True, verbose_name='اضافه کار (ساعت)')  
    # employee_workload_overtime_minutes = models.SmallIntegerField(blank=True, null=True, verbose_name='اضافه کار (دقیقه)')  
    # employee_workload_night_work_hours = models.SmallIntegerField(blank=True, null=True, verbose_name='شب کاری (ساعت)')  
    # employee_workload_night_work_minutes = models.SmallIntegerField(blank=True, null=True, verbose_name='شب کاری (دقیقه)')  
    # employee_workload_holiday_overtime_hours = models.SmallIntegerField(blank=True, null=True, verbose_name='اضافه کار تعطیلات (ساعت)')  
    # employee_workload_holiday_overtime_minutes = models.SmallIntegerField(blank=True, null=True, verbose_name='اضافه کار تعطیلات (دقیقه)')  
    # employee_workload_hourly_leave_hours = models.SmallIntegerField(blank=True, null=True, verbose_name='مرخصی ساعتی (ساعت)')  
    # employee_workload_hourly_leave_minutes = models.SmallIntegerField(blank=True, null=True, verbose_name='مرخصی ساعتی (دقیقه)')  
    # employee_workload_hourly_deduction_hours = models.SmallIntegerField(blank=True, null=True, verbose_name='کسر کار ساعتی (ساعت)')  
    # employee_workload_hourly_deduction_minutes = models.SmallIntegerField(blank=True, null=True, verbose_name='کسر کار ساعتی (دقیقه)')  
    # employee_workload_payslip = models.TextField(blank=True, null=True, verbose_name='توضیحات فیش حقوق')  
    # employee_workload_description = models.TextField(blank=True, null=True, verbose_name='توضیحات کارکرد')  
    # employee_workload_job_group = models.CharField(max_length=50, blank=True, null=True, verbose_name='گروه شغلی')  
    # employee_workload_occasional_payment_used = models.IntegerField(blank=True, null=True, default=0, verbose_name='پرداخت مناسبتی مصرف شده در سال (ریال)')  
    # employee_workload_bonus_calculation_basis = models.SmallIntegerField(blank=True, null=True, verbose_name='مبنا محاسبه پاداش')  
    # employee_workload_employee_status = models.CharField(max_length=50, blank=True, null=True, default="", verbose_name='وضعیت پرسنل')  
    # employee_workload_total_sick_leave_used = models.SmallIntegerField(blank=True, null=True, default=0, verbose_name='مجموع استعلاجی استفاده شده در کل سال')  
    # employee_workload_advance_payment_max = models.BigIntegerField(blank=True, null=True, default=0, verbose_name='سقف مساعده قابل پرداخت')  
    # employee_workload_days_since_last_advance_payment = models.SmallIntegerField(blank=True, null=True, default=0, verbose_name='تعداد روز از آخرین دریافت مساعده')  
    # employee_workload_accepted_degree = models.CharField(max_length=50, blank=True, null=True, default="", verbose_name='مدرک تحصیلی پذیرفته شده')  
    # employee_workload_degree_code = models.CharField(max_length=20, blank=True, null=True, default="", verbose_name='کد مدرک')  
    # employee_workload_work_experience_years = models.SmallIntegerField(blank=True, null=True, default=0, verbose_name='سابقه کار به سال')  
    # employee_workload_specialized_bonus = models.BigIntegerField(blank=True, null=True, default=0, verbose_name='فوق العاده تخصصی (ریال)')  
    # employee_workload_company_debt = models.BigIntegerField(blank=True, null=True, default=0, verbose_name='بدهی به شرکت (ریال)')

    def save(self, *args, **kwargs):
        if self.employee:
            self.employee_workload_first_name = self.employee.employee_first_name
            self.employee_workload_last_name = self.employee.employee_last_name
            self.employee_workload_national_code = self.employee.employee_national_code
            self.employee_workload_personnel_code = self.employee.employee_personnel_code
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.employee_workload_first_name} {self.employee_workload_last_name} {self.employee_workload_working_month}"
        
    class Meta:
        db_table = 'employee_workload'
        verbose_name = 'کارکرد کارمند'
        verbose_name_plural = 'کارکرد پرسنل'