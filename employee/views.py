from django.shortcuts import render
from django.urls import reverse
from django.http import HttpResponseRedirect
from django.views.generic import TemplateView, CreateView, UpdateView, ListView, DetailView
from django.contrib.auth.views import LoginView, LogoutView

from .models import Employee
from .forms import EmployeeCreateForm, EmployeeSalaryUpdateForm

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
        return reverse('update_employee')
    
    def form_valid(self, form):
        self.object = form.save()
        self.request.session['id'] = self.object.id
        return HttpResponseRedirect(self.get_success_url())

class EmployeeSalaryUpdateView(UpdateView):
    model = Employee
    form_class = EmployeeSalaryUpdateForm

    def get_object(self):
        object = self.model.objects.get(id=self.request.session['id'])
        return object
    
    def get_success_url(self):
        return reverse('home')

class EmployeeListView(ListView):
    model = Employee
    context_object_name = 'employees'

class EmployeeDetailView(DetailView):
    model = Employee