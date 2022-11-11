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