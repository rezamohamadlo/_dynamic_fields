from rest_framework import generics
from .models import Employee
from .serializers import EmployeeSerializer
from rest_framework.exceptions import NotFound
from rest_framework.response import Response
from django.shortcuts import render
from rest_framework import status


def employee_list_view(request):
    return render(request, 'employee/employee_list.html')


class EmployeeListCreate(generics.ListCreateAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer


class EmployeeRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer

    def delete(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response({"success": True}, status=status.HTTP_200_OK)