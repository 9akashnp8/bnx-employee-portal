from django.utils import timezone
from django.test import TestCase
from employee.models import Department, Designation, Branch, Employee, CustomUser

class DepartmentModelTest(TestCase):

    def create_department(self, department='Test Department'):
        return Department.objects.create(department=department)
    
    def test_department_str_returns_department_name(self):
        department = self.create_department()
        self.assertTrue(isinstance(department, Department))
        self.assertEqual(department.__str__(), department.department)

class DesignationModelTest(DepartmentModelTest):

    def create_designation(self):
        department = self.create_department()
        return Designation.objects.create(department=department, designation='Test Designation')
    
    def test_designation_str_returns_designation_name(self):
        designation = self.create_designation()
        self.assertTrue(isinstance(designation, Designation))
        self.assertEqual(designation.__str__(), designation.designation)

class BranchModelTest(DesignationModelTest):

    def create_branch(self, branch='Test Branch'):
        return Branch.objects.create(branch=branch)
    
    def test_branch_str_returns_branch_name(self):
        branch = self.create_branch()
        self.assertTrue(isinstance(branch, Branch))
        self.assertEqual(branch.__str__(), branch.branch)

class EmployeeModelTest(BranchModelTest):

    def create_employee(self):
        department = self.create_department()
        designation = self.create_designation()
        branch = self.create_branch()
        return Employee.objects.create(
            employee_code='TEST-001',
            first_name='Test First Name',
            last_name='Test Last Name',
            email='test@gmail.com',
            phone='8075680332',
            department=department,
            designation=designation,
            branch=branch,
            salary=100,
            date_of_joining=timezone.now(),
            date_created=timezone.now(),
            is_active=True
        )
    
    def test_employee_str_returns_employee_code_plus_name(self):
        employee = self.create_employee()
        self.assertTrue(isinstance(employee, Employee))
        self.assertEqual(employee.__str__(), f"{employee.employee_code} - {employee.first_name}")

class CustomUserModelTest(TestCase):

    def create_custom_user(self):
        return CustomUser.objects.create_user(
            email='test@gmail.com',
            password='testPassword'
        )
    
    def test_custom_user_str_returns_custom_user_email(self):
        custom_user = self.create_custom_user()
        self.assertTrue(isinstance(custom_user, CustomUser))
        self.assertEqual(custom_user.__str__(), custom_user.email)