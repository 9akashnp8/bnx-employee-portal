from django.db import models
from django.contrib.auth.models import AbstractUser
from .manager import CustomUserManager

# Create your models here.
class Department(models.Model):
    department = models.CharField(max_length=100)

    def __str__(self):
        return self.department

class Designation(models.Model):
    department = models.ForeignKey(Department, null=True, on_delete=models.SET_NULL)
    designation = models.CharField(max_length=100)
    
    def __str__(self):
        return self.designation

class Branch(models.Model):
    branch = models.CharField(max_length=50)

    def __str__(self):
        return self.branch

class Employee(models.Model):
    employee_code = models.CharField(max_length=50, unique=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(max_length=255, unique=True)
    phone = models.CharField(max_length=20)
    department = models.ForeignKey(Department, null=True, on_delete=models.SET_NULL)
    designation = models.ForeignKey(Designation, null=True, on_delete=models.SET_NULL)
    branch = models.ForeignKey(Branch, null=True, on_delete=models.SET_NULL)
    salary = models.DecimalField(max_digits=20, decimal_places=2, null=True, blank=True)
    date_of_joining = models.DateField()
    date_of_exit = models.DateField(null=True, blank=True)
    date_created = models.DateField(auto_now_add=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.employee_code} - {self.first_name}"

class CustomUser(AbstractUser):
    email = models.EmailField("email address", unique=True)

    objects = CustomUserManager()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.email