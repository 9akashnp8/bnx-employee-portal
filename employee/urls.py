from django.urls import path
from . import views

urlpatterns = [
    path('', views.Home.as_view(), name='home'),
    path('employee/add/', views.EmployeeCreateView.as_view(), name='add_employee'),
]