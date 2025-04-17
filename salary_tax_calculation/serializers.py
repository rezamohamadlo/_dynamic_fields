# your_app/serializers.py
from rest_framework import serializers
from .models import SalaryTaxCalculation

class SalaryTaxCalculationSerializer(serializers.ModelSerializer):
    class Meta:
        model = SalaryTaxCalculation
        fields = '__all__'