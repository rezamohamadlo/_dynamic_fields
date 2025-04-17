from rest_framework import generics
from .models import SalaryCalculation
from .serializers import SalaryCalculationSerializers
from rest_framework.exceptions import NotFound


class SalaryCalculationListCreate(generics.ListCreateAPIView):
    queryset = SalaryCalculation.objects.all()
    serializer_class = SalaryCalculationSerializers



class SalaryCalculationRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = SalaryCalculation.objects.all()
    serializer_class = SalaryCalculationSerializers