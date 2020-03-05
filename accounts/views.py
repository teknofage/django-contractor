from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from .forms import ProfileSetupForm
from django.urls import reverse_lazy, reverse
from django.views.generic import CreateView, TemplateView
from django.http import HttpResponseRedirect

# Create your views here.
class SignUpView(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'
    
    
class LogInView(TemplateView):
    template_name = 'registration/login.html'
    success_url = reverse_lazy('profile-home')
    
class ProfileSetupView(CreateView):
    template_name = 'registration/profile-setup.html'
    form_class = ProfileSetupForm
    success_url = reverse_lazy('login')
    
    def post(self, request):
        form = ProfileSetupForm(request.POST)
        if form.is_valid():
            profile = form.save(commit=False)
            profile.user = request.user
            profile.save()
            return HttpResponseRedirect(reverse('home-view'))
        print("smarties")
        return render(request, 'registration/profile-setup.html', context={"form":form})
    
    def form_valid(self, form):
        return True
    
class HomeView(TemplateView):
    template_name = 'home-view.html'