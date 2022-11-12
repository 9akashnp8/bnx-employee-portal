from django.contrib.auth.forms import UserCreationForm, UserChangeForm, AuthenticationForm
from django.contrib.auth.models import User
from django import forms
from django.forms import DateInput

from .models import CustomUser, Employee

class LoginForm(AuthenticationForm):
    
    def __init__(self, request=None, *args, **kwargs):
        # self.request = request
        super(LoginForm, self).__init__(*args, **kwargs)
        self.fields["username"].widget.attrs.update({'class': 'form-field'})
        self.fields["password"].widget.attrs.update({'class': 'form-field'})

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
        widgets = {
            'date_of_joining': DateInput(attrs={'type':'date'}),
            'date_of_exit': DateInput(attrs={'type':'date'})
        }
    
    def __init__(self, *args, **kwargs):
        super(EmployeeCreateForm, self).__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs.update({'class': 'form-field'})

class EmployeeSalaryUpdateForm(forms.ModelForm):
    employee_code = forms.CharField(max_length=50, disabled=True)
    first_name = forms.CharField(max_length=50, disabled=True)

    class Meta:
        model = Employee
        fields = ['employee_code', 'first_name', 'salary']
    
    def __init__(self, *args, **kwargs):
        super(EmployeeSalaryUpdateForm, self).__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs.update({'class': 'form-field'})