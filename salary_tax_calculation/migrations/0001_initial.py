# Generated by Django 5.2 on 2025-04-17 19:03

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('employee', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='SalaryTaxCalculation',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('salary_tax_calculation_salary', models.DecimalField(decimal_places=0, max_digits=16, verbose_name='حقوق')),
                ('salary_tax_calculation_calculated_tax', models.DecimalField(blank=True, decimal_places=0, default=0, editable=False, max_digits=16, null=True, verbose_name='مالیات محاسبه شده')),
                ('salary_tax_calculation_employee', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='employee.employee')),
            ],
        ),
    ]
