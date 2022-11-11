from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django import forms

from .models import CustomUser, Employee

class SignUpForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ('email',)

class UserUpdateForm(UserChangeForm):
    class Meta:
        model = CustomUser
        fields = ('email',)

class EmployeeCreateForm(forms.ModelForm):
    class Meta:
        model = Employee
        exclude = ['salary']

class EmployeeSalaryUpdateForm(forms.ModelForm):
    employee_code = forms.CharField(max_length=50, disabled=True)
    first_name = forms.CharField(max_length=50, disabled=True)
    class Meta:
        model = Employee
        fields = ['employee_code', 'first_name', 'salary']