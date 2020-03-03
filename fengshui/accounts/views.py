from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views.generic import CreateView, TemplateView

# Create your views here.
class SignUpView(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'
    
    
class LogInView(TemplateView):
    template_name = 'registration/login.html'
    success_url = reverse_lazy('profile-home')
    
class ProfileHomeView(TemplateView):
    template_name = 'registration/profile-home.html'