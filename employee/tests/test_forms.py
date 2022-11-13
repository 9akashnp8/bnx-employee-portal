from django.test import SimpleTestCase

from employee.forms import (
    EmployeeCreateForm, LoginForm, EmployeeUpdateForm
)
from employee.models import (
    Employee, Department, Designation, Branch
)

class TestEmployeeAppForms(SimpleTestCase):

    databases = '__all__'

    def setUp(self):
        self.department = Department.objects.create(department='test department')
        self.designation = Designation.objects.create(department=self.department, designation='test designation')
        self.branch = Branch.objects.create(branch='test branch')

    def test_employee_create_form_valid_data(self):
        form = EmployeeCreateForm(data={
            'employee_code': 'BNX-02',
            'first_name': 'Akash',
            'last_name': 'NP',
            'email': 'test@test.com',
            'phone': '8075680336',
            'department': self.department,
            'designation': self.designation,
            'branch': self.branch,
            'salary': 50000,
            'date_of_joining': '2022-11-12',
            'date_created': '2022-11-12',
            'is_active': True
        })

        self.assertTrue(form.is_valid())
    
    def test_employee_create_no_form_data(self):
        form = EmployeeCreateForm(data={})
        self.assertFalse(form.is_valid())
        self.assertEqual(len(form.errors), 9)
    
    def test_employee_create_form_invalid_data(self):
        pass # To Do

    def test_employee_update_form_valid_data(self):
        form = EmployeeUpdateForm(data={
            'employee_code': 'BNX-02',
            'first_name': 'Akash',
            'last_name': 'NP',
            'email': 'test@test.com',
            'phone': '8075680336',
            'department': self.department,
            'designation': self.designation,
            'branch': self.branch,
            'salary': 50000,
            'date_of_joining': '2022-11-12',
            'date_created': '2022-11-12',
            'is_active': True
        })

        self.assertTrue(form.is_valid())
    
    def test_employee_update_form_invalid_data(self):
        form = EmployeeUpdateForm(data={
            'employee_code': 'DNX-02', # Invalid Employee Code
            'first_name': 'Akash',
            'last_name': 'NP',
            'email': 'test@test', # Invalid Email
            'phone': '8075680336',
            'department': self.department,
            'designation': self.designation,
            'branch': self.branch,
            'salary': 50000,
            'date_of_joining': '12-11-2022', # Invalid Date
            'date_created': '12-11-2022', # Invalid Date
            'is_active': True
        })
        self.assertFalse(form.is_valid())
        form_errors = [form.errors[error][0] for error in form.errors]
        self.assertIn(
            "Employee Code Error. Code must be of format: 'BNX-000'. Eg: 'BNX-001'", 
            form_errors 
        )
        self.assertIn('Enter a valid email address.', form_errors )
        self.assertIn('Enter a valid date.', form_errors )



class TestLoginForm(SimpleTestCase):

    def test_login_form_has_custom_class_set_from_init_(self):
        form = LoginForm()

        fields_have_custom_class = {
            'username': False,
            'password': False
        }

        for field in form.fields:
            if form.fields[field].widget.attrs['class'] == 'form-field text-black':
                fields_have_custom_class[field] = True

        self.assertEqual(fields_have_custom_class['username'], True)
        self.assertEqual(fields_have_custom_class['password'], True)
    
