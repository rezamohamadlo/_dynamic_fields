from rest_framework import generics
from .models import EmployeeWorkload
from .serializers import EmployeeWorkloadSerializer
from rest_framework.exceptions import NotFound

class EmployeeWorkloadListCreate(generics.ListCreateAPIView):
    queryset = EmployeeWorkload.objects.all()
    serializer_class = EmployeeWorkloadSerializer



class EmployeeWorkloadRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = EmployeeWorkload.objects.all()  # Important: Keep this for other methods (update/retrieve)
    serializer_class = EmployeeWorkloadSerializer