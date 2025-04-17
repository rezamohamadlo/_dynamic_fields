# your_app/serializers.py
from rest_framework import serializers
from .models import WorkingMonth

class WorkingMonthSerializer(serializers.ModelSerializer):
    class Meta:
        model = WorkingMonth
        fields = '__all__'