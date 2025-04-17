from django.urls import path
from .views import EmployeeListCreate, EmployeeRetrieveUpdateDestroy
from . import views  

urlpatterns = [
    path('', EmployeeListCreate.as_view(), name='employee_list_create'),
    path('<int:pk>/', EmployeeRetrieveUpdateDestroy.as_view(), name='employee_detail'),
    path('employee_view/', views.employee_list_view,  
         name='employee-list'),  
]