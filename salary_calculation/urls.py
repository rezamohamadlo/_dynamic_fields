from django.urls import path
from .views import SalaryCalculationListCreate, SalaryCalculationRetrieveUpdateDestroy


urlpatterns = [
    path('', SalaryCalculationListCreate.as_view(), name='salary_calculation_list_create'),
    path('<int:pk>/', SalaryCalculationRetrieveUpdateDestroy.as_view(), name='salary_calculation_detail'),
]