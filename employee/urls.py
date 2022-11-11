from django.urls import path
from . import views

urlpatterns = [
    path('', views.Home.as_view(), name='home'),
    path('employee/add/', views.EmployeeCreateView.as_view(), name='add_employee'),
    path('employee/add/salary/', views.EmployeeSalaryUpdateView.as_view(), name='update_employee'),
    path('employees/', views.EmployeeListView.as_view(), name='list_employee'),
]