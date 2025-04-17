
from django.db import models
# from marital_status.models import MaritalStatus
# from degree.models import Degree
# from gender.models import Gender
# from military_status.models import MilitaryStatus
# from city.models import City
from django.utils import timezone
# from industry.models import Industry
# from job_level.models import JobLevel
# from job_nature.models import JobNature
# from job_title.models import JobTitle
# from country.models import Country
# from bank.models import Bank


class Employee(models.Model):
    id = models.BigAutoField(primary_key=True)
    employee_national_code = models.CharField(max_length=10, blank=True, null=True)
    employee_first_name = models.CharField(max_length=50, blank=True, null=True)
    employee_last_name = models.CharField(max_length=50, blank=True, null=True)
    # employee_service_place = models.ForeignKey(Industry, on_delete=models.PROTECT, blank=True, null=True)
    employee_personnel_code = models.CharField(max_length=50, blank=True, null=True)
    # employee_nationality = models.ForeignKey(Country, on_delete=models.PROTECT, blank=True, null=True, related_name='nationality_employee')
    # employee_citizenship = models.ForeignKey(Country, on_delete=models.PROTECT, blank=True, null=True, related_name='citizenship_employee')
    # employee_living_country = models.ForeignKey(Country, on_delete=models.PROTECT, blank=True, null=True, related_name='living_employee')
    # employee_marital_status = models.ForeignKey(MaritalStatus, on_delete=models.PROTECT, blank=True, null=True)
    # employee_employment_start_date = models.DateField(blank=True, null=True)
    # employee_employment_end_date = models.DateField(blank=True, null=True)
    # employee_job_title_insurance_code = models.CharField(max_length=50, blank=True, null=True)
    # employee_degree = models.ForeignKey(Degree, on_delete=models.PROTECT, null=True, blank=True)
    # employee_field_of_study = models.CharField(max_length=50, blank=True, null=True)
    # employee_father_name = models.CharField(max_length=50, blank=True, null=True)
    # employee_birth_date = models.DateField(default=timezone.now, blank=True, null=True)
    # employee_birth_place = models.ForeignKey(City, on_delete=models.PROTECT, null=True, blank=True)
    # employee_place_of_issue = models.CharField(max_length=50, blank=True, null=True)
    # employee_birth_certificate_serial = models.CharField(max_length=10, blank=True, null=True)
    # employee_birth_certificate_number = models.CharField(max_length=20, blank=True, null=True)
    # employee_gender = models.ForeignKey(Gender, on_delete=models.PROTECT, null=True, blank=True)
    # employee_number_of_children = models.SmallIntegerField(blank=True, null=True)
    # employee_disabled_children_number = models.SmallIntegerField(blank=True, null=True)
    # employee_peyvand_children_number = models.SmallIntegerField(blank=True, null=True)
    # employee_employment_type = models.CharField(max_length=50, blank=True, null=True)
    # employee_espadana_employment_date = models.DateField(blank=True, null=True)
    # employee_military_status = models.ForeignKey(MilitaryStatus, on_delete=models.PROTECT, null=True, blank=True)
    # employee_internal_job_title = models.CharField(max_length=50, blank=True, null=True)
    # employee_job_title = models.ForeignKey(JobTitle, on_delete=models.PROTECT, blank=True, null=True)
    # employee_job_nature = models.ForeignKey(JobNature, on_delete=models.PROTECT, blank=True, null=True)
    # employee_job_level = models.ForeignKey(JobLevel, on_delete=models.PROTECT, blank=True, null=True)
    # employee_address = models.TextField(blank=True, null=True)
    # employee_postal_code = models.CharField(max_length=10, blank=True, null=True)
    # employee_landline_number = models.CharField(max_length=20, blank=True, null=True)
    # employee_phone_number = models.CharField(max_length=20, blank=True, null=True)
    # employee_tamin_insurance_number = models.CharField(max_length=50, blank=True, null=True)
    # employee_kosar_insurance_number = models.CharField(max_length=50, blank=True, null=True)
    # employee_email = models.CharField(max_length=50, blank=True, null=True)
    # employee_work_experience_year = models.SmallIntegerField(blank=True, null=True)
    # employee_work_experience_month = models.SmallIntegerField(blank=True, null=True)
    # employee_work_experience_day = models.SmallIntegerField(blank=True, null=True)
    # employee_sacrifice_status = models.BooleanField(default=False, blank=True, null=True)
    # employee_workshop_insurance_code = models.CharField(max_length=20, blank=True, null=True)
    # employee_insurance_start_date = models.DateField(blank=True, null=True)
    # employee_insurance_end_date = models.DateField(blank=True, null=True)
    # employee_work_leave_date = models.DateField(blank=True, null=True)
    # employee_hard_work = models.BooleanField(blank=True, null=True)
    # employee_include_in_tamin = models.BooleanField(blank=True, null=True)
    # employee_insurance_type = models.CharField(max_length=50, blank=True, null=True)
    # employee_supplementary_insurance_type = models.CharField(max_length=50, blank=True, null=True)
    # employee_service_place_status = models.CharField(max_length=50, blank=True, null=True)
    # employee_tax_exemption_type = models.CharField(max_length=50, blank=True, null=True)
    # employee_budget_law_exemption = models.CharField(max_length=50, blank=True, null=True)
    # employee_house_usage_status = models.CharField(blank=True, null=True, max_length=50, choices=[('استفاده از مسکن', 'استفاده از مسکن'), ('عدم استفاده از مسکن', 'عدم استفاده از مسکن')])
    # employee_car_usage_status = models.CharField(blank=True, null=True, max_length=50, choices=[('استفاده از خودرو', 'استفاده از خودرو'), ('عدم استفاده از خودرو', 'عدم استفاده از خودرو')])
    # employee_include_in_tax_documents = models.BooleanField(blank=True, null=True)
    # employee_bank = models.ForeignKey(Bank, on_delete=models.PROTECT, blank=True, null=True)
    # employee_bank_account_number = models.CharField(max_length=50, blank=True, null=True)
    # employee_tax_start_date = models.DateField(blank=True, null=True)
    # employee_tax_end_date = models.DateField(blank=True, null=True)

    class Meta:
        db_table = 'employee'


    def __str__(self):
        return f"{self.employee_first_name} {self.employee_last_name}"# {self.employee_service_place})"