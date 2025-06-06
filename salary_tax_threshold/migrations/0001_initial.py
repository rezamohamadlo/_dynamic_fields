# Generated by Django 5.2 on 2025-04-17 19:03

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='SalaryTaxThreshold',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('salary_tax_threshold_amount', models.DecimalField(decimal_places=0, default=0, max_digits=16, verbose_name='مبلغ مبنا')),
                ('salary_tax_threshold_percentage', models.DecimalField(decimal_places=2, default=0, max_digits=5, verbose_name='درصد')),
                ('salary_tax_threshold_base_year', models.DateField(default='1403-01-01')),
            ],
            options={
                'db_table': 'salary_tax_threshold',
            },
        ),
    ]
