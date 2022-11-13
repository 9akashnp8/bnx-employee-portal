import json
from django.utils import timezone
from django.test import TestCase, Client
from django.urls import reverse
from employee.models import Employee, Department, Designation, Branch

class TestViews(TestCase):

    def setUp(self):
        self.department = Department.objects.create(department='test_department')
        self.designation = Designation.objects.create(department=self.department, designation='test_designation')
        self.branch = Branch.objects.create(branch='test_branch')
        self.employee = Employee.objects.create(
            employee_code='BNX-001',
            first_name='Akash',
            last_name='NP',
            email='akash@gmail.com',
            phone='8075680338',
            department=self.department,
            designation=self.designation,
            branch=self.branch,
            salary=50000,
            date_of_joining=timezone.now(),
            date_created=timezone.now(),
            is_active=True
        )
        self.client = Client()
        self.home_url = reverse('home')
        self.add_url = reverse('add_employee')
        self.update_salary_url = reverse('update_employee_salary')
        self.list_url = reverse('list_employee')
        self.detail_url = reverse('detail_employee', args=[self.employee.id])
        self.update_url = reverse('update_employee', args=[self.employee.id])
        self.delete_url = reverse('delete_employee', args=[self.employee.id])
    
    def test_home_GET(self):
        response = self.client.get(self.home_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'home.html')
    
    def test_add_employee_GET(self):
        response = self.client.get(self.add_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'employee/employee_form.html')

    def test_update_employee_salary_GET(self):
        session = self.client.session
        session['id'] = self.employee.id
        session.save()
        response = self.client.get(self.update_salary_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'employee/employee_form.html')

    def test_list_employee_GET(self):
        response = self.client.get(self.list_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'employee/employee_list.html')

    def test_detail_employee_GET(self):
        response = self.client.get(self.detail_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'employee/employee_detail.html')

    def test_update_employee_GET(self):
        response = self.client.get(self.update_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'employee/employee_form.html')

    def test_delete_employee_GET(self):
        response = self.client.get(self.delete_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'employee/employee_confirm_delete.html')
    
    def test_add_employee_POST_with_valid_data(self):
        response = self.client.post(self.add_url, {
            'employee_code': 'BNX-02',
            'first_name': 'Akash',
            'last_name': 'NP',
            'email': 'test@test.com',
            'phone': '8075680336',
            'department': str(self.department.id),
            'designation': str(self.designation.id),
            'branch': str(self.branch.id),
            'salary': 50000,
            'date_of_joining': '2022-11-12',
            'date_created': '2022-11-12',
            'is_active': True
        })
        self.assertEqual(response.status_code, 302)
        self.assertEqual(Employee.objects.count(), 2)
    
    def test_add_employee_POST_with_invalid_data(self):
        response = self.client.post(self.add_url, {
            'employee_code': 'DNX-02', # Invalid Employee Code
            'first_name': 'Akash',
            'last_name': 'NP',
            'email': 'test@test', # Invalid Email
            'phone': '8075680336',
            'department': str(self.department.id),
            'designation': str(self.designation.id),
            'branch': str(self.branch.id),
            'salary': "50000",
            'date_of_joining': '12-11-2022', # Wrong date format
            'date_created': '12-11-2022', # Wrong date format
            'is_active': True
        })
        self.assertContains(response, "Employee Code Error")
        self.assertContains(response, "Enter a valid date")
        self.assertContains(response, "Enter a valid email address")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(Employee.objects.count(), 1)
    
    def test_add_employee_POST_without_data(self):
        response = self.client.post(self.add_url, {})
        self.assertContains(response, "This field is required")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(Employee.objects.count(), 1)
    
    def test_update_salary_employee_POST_valid_data(self):
        session = self.client.session
        session['id'] = self.employee.id
        session.save()
        response = self.client.post(self.update_salary_url, {
            'employee_code': self.employee.id,
            'first_name': self.employee.first_name,
            'salary': 50000
        })
        self.assertEqual(response.status_code, 302)
        self.assertEqual(response.url, reverse('detail_employee', args=[self.employee.id]))

    def test_update_employee_POST_valid_data(self):
        response = self.client.post(self.update_url, {
            'employee_code': 'BNX-03',
            'first_name': 'Akshay',
            'last_name': 'NP',
            'email': 'test@test2.com',
            'phone': '8075680346',
            'department': str(self.department.id),
            'designation': str(self.designation.id),
            'branch': str(self.branch.id),
            'salary': 55000,
            'date_of_joining': '2022-11-12',
            'date_created': '2022-11-12',
            'is_active': True
        })
        self.assertEqual(response.status_code, 302)
        self.assertEqual(response.url, reverse('detail_employee', args=[self.employee.id]))

