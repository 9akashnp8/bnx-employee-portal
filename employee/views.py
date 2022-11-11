from django.shortcuts import render
from django.views.generic import TemplateView
from django.contrib.auth.views import LoginView, LogoutView

# Create your views here.
class Home(TemplateView):
    template_name = 'home.html'

class CustomLoginView(LoginView):
    next_page = 'home'

class CustomLogoutView(LogoutView):
    next_page = 'login'
