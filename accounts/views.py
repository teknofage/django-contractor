from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.mixins import UserPassesTestMixin
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse_lazy, reverse
from django.views.generic import CreateView, TemplateView, UpdateView, DeleteView
from .forms import ProfileSetupForm, ProfileUpdateForm
from .models import Profile
from accounts.models import Direction

# Create your views here.
class SignUpView(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'
    success_message = "Congratulations! You may now log in to Peach Blossom Love Calculator."

    
class LogInView(TemplateView):
    template_name = 'registration/login.html'
    success_url = reverse_lazy('profile-home')
    
    def form_completed(self, form):
        if profile.user == True:
            return render(request, 'home-view.html', {'profile':profile_data})
        else:
            return render(request, 'registration/profile-setup.html', context={"form":form})
    
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
            return HttpResponseRedirect(reverse_lazy('home-view'))#, kwargs={"form":form}))
        print(form)
        return render(request, 'registration/profile-setup.html', context={"form":form})
    
class HomeView(TemplateView):
    template_name = 'home-view.html'

    def get(self, request, *args, **kwargs):
        current_user = request.user
        profile_data = Profile.objects.get(user=current_user)
        return render(request, 'home-view.html', {'profile':profile_data})
    
    def test_func(self):
        '''Ensures that users can only view their own Profiles.'''
        user = Profile.get_object()
        return (Profile.request.user.profile == user.profile)

class ProfileUpdateView(UserPassesTestMixin, UpdateView):
    '''User is allowed to change their own account information.'''
    form_class = ProfileUpdateForm
    model = Profile
    template_name = 'registration/profile-update.html'
    # fields = ['date_of_birth', 'zodiac_animal', 'gender']
    queryset = Profile.objects.all()
    
    def post(self, request):
        form = ProfileUpdateForm(request.POST)
        if form.is_valid():
            profile = form.save(commit=False)
            profile.user = request.user
            profile.save()
            return HttpResponseRedirect(reverse_lazy('home-view'))#, kwargs={"form":form}))
        print(form)
        return render(request, 'registration/profile-setup.html', context={"form":form})

    def get_success_url(self):
        '''Redirect to the profile page of the User.'''
        url = self.object.profile.get_absolute_url()
        return url

    def test_func(self):
        '''Ensure only the User can change their own account information.'''
        user = self.get_object()
        return (self.request.user == user)
    
        