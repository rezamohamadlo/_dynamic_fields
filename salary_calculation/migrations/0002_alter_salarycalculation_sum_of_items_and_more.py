# Generated by Django 5.2 on 2025-04-17 05:52

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('salary_calculation', '0001_initial'),
        ('salary_item', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='salarycalculation',
            name='sum_of_items',
            field=models.DecimalField(decimal_places=2, default=0, editable=False, max_digits=16),
        ),
        migrations.AlterModelTable(
            name='salarycalculation',
            table=None,
        ),
        migrations.CreateModel(
            name='SalaryCalculationItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.DecimalField(decimal_places=2, max_digits=16)),
                ('calculation', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='items', to='salary_calculation.salarycalculation')),
                ('salary_item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='salary_item.salaryitem')),
            ],
        ),
    ]
