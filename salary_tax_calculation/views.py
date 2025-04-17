from rest_framework import generics
from .models import SalaryTaxCalculation
from .serializers import SalaryTaxCalculationSerializer
from rest_framework.exceptions import NotFound

class SalaryTaxCalculationListCreate(generics.ListCreateAPIView):
    queryset = SalaryTaxCalculation.objects.all()
    serializer_class = SalaryTaxCalculationSerializer



class SalaryTaxCalculationRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = SalaryTaxCalculation.objects.all()
    serializer_class = SalaryTaxCalculationSerializer