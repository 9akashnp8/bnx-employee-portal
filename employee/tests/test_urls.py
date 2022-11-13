from django.test import SimpleTestCase
from django.urls import reverse, resolve

from employee.views import  (
    Home, EmployeeCreateView, EmployeeSalaryUpdateView, EmployeeListView,
    EmployeeDetailView, EmployeeDeleteView, CustomLoginView, CustomLogoutView,
    EmployeeUpdateView
)

class TestEmployeeAppUrls(SimpleTestCase):

    def test_home_url_is_resolves(self):
        url = reverse('home')
        self.assertEqual(resolve(url).func.__name__, Home.as_view().__name__)
    
    def test_add_employee_url_is_resolves(self):
        url = reverse('add_employee')
        self.assertEqual(resolve(url).func.__name__, EmployeeCreateView.as_view().__name__)

    def test_update_employee_salary_url_is_resolves(self):
        url = reverse('update_employee_salary')
        self.assertEqual(resolve(url).func.__name__, EmployeeSalaryUpdateView.as_view().__name__)
    
    def test_list_employee_url_is_resolves(self):
        url = reverse('list_employee')
        self.assertEqual(resolve(url).func.__name__, EmployeeListView.as_view().__name__)

    def test_detail_employee_url_is_resolves(self):
        url = reverse('detail_employee', args=[1])
        self.assertEqual(resolve(url).func.__name__, EmployeeDetailView.as_view().__name__)

    def test_update_employee_url_is_resolves(self):
        url = reverse('update_employee', args=[1])
        self.assertEqual(resolve(url).func.__name__, EmployeeUpdateView.as_view().__name__)

    def test_delete_employee_url_is_resolves(self):
        url = reverse('delete_employee', args=[1])
        self.assertEqual(resolve(url).func.__name__, EmployeeDeleteView.as_view().__name__)

class TestProjectUrls(SimpleTestCase):

    def test_login_url_is_resolves(self):
        url = reverse('login')
        self.assertEqual(resolve(url).func.view_class, CustomLoginView)

    def test_logout_url_is_resolves(self):
        url = reverse('logout')
        self.assertEqual(resolve(url).func.view_class, CustomLogoutView )

