from rest_framework import serializers
from .models import SalaryCalculation, SalaryCalculationItem
from salary_item.models import SalaryItem

class SalaryCalculationItemSerializer(serializers.ModelSerializer):
    # Optionally, include salary item details
    salary_item_name = serializers.ReadOnlyField(source='salary_item.english_name')

    class Meta:
        model = SalaryCalculationItem
        # fields = ['id', 'salary_item', 'salary_item_name', 'amount']
        fields = ['id', 'salary_item', 'salary_item_name', 'amount']

class SalaryCalculationSerializers(serializers.ModelSerializer):
    items = SalaryCalculationItemSerializer(many=True)

    class Meta:
        model = SalaryCalculation
        # fields = ['id', 'sum_of_items', 'items']
        fields = '__all__'
    def create(self, validated_data):
        items_data = validated_data.pop('items')
        calculation = SalaryCalculation.objects.create(**validated_data)
        for item_data in items_data:
            SalaryCalculationItem.objects.create(calculation=calculation, **item_data)
        calculation.update_total()
        return calculation

    def update(self, instance, validated_data):
        items_data = validated_data.pop('items')
        # Update calculation fields if any
        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        instance.save()

        # Update related items
        # Simple approach: delete old items and create new ones
        instance.items.all().delete()
        for item_data in items_data:
            SalaryCalculationItem.objects.create(calculation=instance, **item_data)

        instance.update_total()
        return instance

