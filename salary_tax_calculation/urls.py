from django.urls import path
from .views import SalaryTaxCalculationListCreate, SalaryTaxCalculationRetrieveUpdateDestroy


urlpatterns = [
    path('', SalaryTaxCalculationListCreate.as_view(), name='salary_tax_calculation_list_create'),
    path('<int:pk>/', SalaryTaxCalculationRetrieveUpdateDestroy.as_view(), name='salary_tax_calculation_detail'),
]