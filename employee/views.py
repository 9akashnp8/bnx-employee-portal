from django.shortcuts import render
from django.urls import reverse
from django.views.generic import TemplateView, CreateView
from django.contrib.auth.views import LoginView, LogoutView

from .models import Employee
from .forms import EmployeeCreateForm

# Common Views
class Home(TemplateView):
    template_name = 'home.html'

class CustomLoginView(LoginView):
    next_page = 'home'

class CustomLogoutView(LogoutView):
    next_page = 'login'

# App Views
class EmployeeCreateView(CreateView):
    model = Employee
    form_class = EmployeeCreateForm
    
    def get_success_url(self):
        return reverse('home')

