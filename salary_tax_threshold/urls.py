from django.urls import path
from .views import SalaryTaxThresholdListCreate, SalaryTaxThresholdRetrieveUpdateDestroy


urlpatterns = [
    path('', SalaryTaxThresholdListCreate.as_view(), name='salary_tax_threshold_list_create'),
    path('<int:pk>/', SalaryTaxThresholdRetrieveUpdateDestroy.as_view(), name='salary_tax_threshold_detail'),
]