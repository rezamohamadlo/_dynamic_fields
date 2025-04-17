from django.urls import path
from .views import EmployeeWorkloadListCreate, EmployeeWorkloadRetrieveUpdateDestroy


urlpatterns = [
    path('', EmployeeWorkloadListCreate.as_view(), name='employee_workload_list_create'),
    path('<int:pk>/', EmployeeWorkloadRetrieveUpdateDestroy.as_view(), name='employee_workload_detail'),
]