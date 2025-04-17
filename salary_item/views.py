from rest_framework import generics
from .models import SalaryItem
from .serializers import SalaryItemSerializers
from rest_framework.exceptions import NotFound


class SalaryItemListCreate(generics.ListCreateAPIView):
    queryset = SalaryItem.objects.all()
    serializer_class = SalaryItemSerializers



class SalaryItemRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = SalaryItem.objects.all()
    serializer_class = SalaryItemSerializers