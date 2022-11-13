from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()

# API routes
router.register(r'department', views.DepartmentViewSet, basename='department')
router.register(r'designation', views.DesignationViewSet, basename='designation')
router.register(r'branch', views.BranchViewSet, basename='branch')
router.register(r'employee', views.EmployeeViewSet, basename='employee')

urlpatterns = [
    path('', views.Home.as_view(), name='home'),
    path('employee/add/', views.EmployeeCreateView.as_view(), name='add_employee'),
    path('employee/add/salary/', views.EmployeeSalaryUpdateView.as_view(), name='update_employee_salary'),
    path('employees/', views.EmployeeListView.as_view(), name='list_employee'),
    path('employee/<int:pk>', views.EmployeeDetailView.as_view(), name='detail_employee'),
    path('employee/<int:pk>/update/', views.EmployeeUpdateView.as_view(), name='update_employee'),
    path('employee/<int:pk>/delete/', views.EmployeeDeleteView.as_view(), name='delete_employee'),
    path('api/', include(router.urls)),
]