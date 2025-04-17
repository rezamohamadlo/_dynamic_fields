# your_app/serializers.py
from rest_framework import serializers
from .models import EmployeeWorkload

class EmployeeWorkloadSerializer(serializers.ModelSerializer):
    class Meta:
        model = EmployeeWorkload
        fields = '__all__'