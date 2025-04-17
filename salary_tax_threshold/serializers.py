# your_app/serializers.py
from rest_framework import serializers
from .models import SalaryTaxThreshold

class SalaryTaxThresholdSerializer(serializers.ModelSerializer):
    class Meta:
        model = SalaryTaxThreshold
        fields = '__all__'