from django.urls import path
from . import views

urlpatterns = [
    path('', views.Home.as_view(), name='home'),
    path('employee/add/', views.EmployeeCreateView.as_view(), name='add_employee'),
    path('employee/add/salary/', views.EmployeeSalaryUpdateView.as_view(), name='update_employee'),
    path('employees/', views.EmployeeListView.as_view(), name='list_employee'),
    path('employee/<int:pk>', views.EmployeeDetailView.as_view(), name='detail_employee'),
    path('employee/<int:pk>/update/', views.EmployeeUpdateView.as_view(), name='update_employee'),
    path('employee/<int:pk>/delete/', views.EmployeeDeleteView.as_view(), name='delete_employee'),
]