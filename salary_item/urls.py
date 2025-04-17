from django.urls import path
from .views import SalaryItemListCreate, SalaryItemRetrieveUpdateDestroy


urlpatterns = [
    path('', SalaryItemListCreate.as_view(), name='salary_item_list_create'),
    path('<int:pk>/', SalaryItemRetrieveUpdateDestroy.as_view(), name='salary_item_detail'),
]