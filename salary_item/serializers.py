from rest_framework import serializers
from .models import SalaryItem

class SalaryItemSerializers(serializers.ModelSerializer):
    class Meta:
        model = SalaryItem
        fields = '__all__'