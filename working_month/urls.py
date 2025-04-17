from django.urls import path
from .views import WorkingMonthListCreate, WorkingMonthRetrieveUpdateDestroy


urlpatterns = [
    path('', WorkingMonthListCreate.as_view(), name='working_month_list_create'),
    path('<int:pk>/', WorkingMonthRetrieveUpdateDestroy.as_view(), name='working_month_detail'),
]