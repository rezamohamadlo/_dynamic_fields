# Generated by Django 5.2 on 2025-04-17 19:06

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employee_workload', '0002_alter_employeeworkload_employee_workload_working_month'),
        ('working_month', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employeeworkload',
            name='employee_workload_working_month',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='working_month.workingmonth', verbose_name='ماه کاری'),
        ),
    ]
