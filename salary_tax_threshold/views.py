from rest_framework import generics
from .models import SalaryTaxThreshold
from .serializers import SalaryTaxThresholdSerializer
from rest_framework.exceptions import NotFound

class SalaryTaxThresholdListCreate(generics.ListCreateAPIView):
    queryset = SalaryTaxThreshold.objects.all()
    serializer_class = SalaryTaxThresholdSerializer



class SalaryTaxThresholdRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = SalaryTaxThreshold.objects.all()
    serializer_class = SalaryTaxThresholdSerializer