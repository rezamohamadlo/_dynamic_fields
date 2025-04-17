from rest_framework import generics
from .models import WorkingMonth
from .serializers import WorkingMonthSerializer
from rest_framework.exceptions import NotFound

class WorkingMonthListCreate(generics.ListCreateAPIView):
    queryset = WorkingMonth.objects.all()
    serializer_class = WorkingMonthSerializer



class WorkingMonthRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = WorkingMonth.objects.all()
    serializer_class = WorkingMonthSerializer