from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.mixins import UserPassesTestMixin
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse_lazy, reverse
from django.views.generic import CreateView, TemplateView
from .models import Profile
from django.views.generic.edit import (
    CreateView,
    UpdateView,
    DeleteView)
from .forms import ProfileSetupForm

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
            return HttpResponseRedirect(reverse_lazy('home-view'))#, kwargs={"form":form}))
        print(form)
        return render(request, 'registration/profile-setup.html', context={"form":form})
    
    def form_completed(self, form):
        # if form is already completed, take user directly from login to home-view, skipping profile-setup.
        pass
    
class HomeView(TemplateView):
    template_name = 'home-view.html'
    model = Profile
    template_name = 'accounts/profile/view.html'
    login_url = 'accounts:login'
    queryset = User.objects.all()

    def get_context_data(self, request):
        
        user = self.queryset.get(id=pk)
        context = super().get_context_data(**kwargs)
        context["form"] = {"zodiac_animal": user.zodiac_animal, "date_of_birth": "asdf", "gender":"asd"}
        return context
    
        
class AccountUpdate(UserPassesTestMixin, UpdateView):
    '''User is allowed to change their own account information.'''
    model = User
    template_name = 'registration/profile-setup.html'
    fields = ['date_of_birth', 'zodiac_animal', 'gender']
    queryset = User.objects.all()

    def get_success_url(self):
        '''Redirect to the profile page of the User.'''
        url = self.object.profile.get_absolute_url()
        return url

    def test_func(self):
        '''Ensure only the User can change their own account information.'''
        user = self.get_object()
        return (self.request.user == user)
    
        
class UserDelete(UserPassesTestMixin, DeleteView):
    '''User is able to delete their own account from the database.'''
    model = User
    template_name = 'accounts/profile/delete.html'
    success_url = reverse_lazy('accounts:login')
    

    def get(self, request, pk):
        """Renders a page with a form to delete the User account.
        Parameters:
        request(HttpRequest): request sent to the server from the client
        pk(int): the value of the id field of the specific User instance
        Returns:
        HttpResponse: the TemplateResponse with the delete form
        """
        user = self.get_queryset().get(id=pk)
        return render(request, self.template_name)

    def test_func(self):
        '''Ensure that only users can delete their own accounts on the site.'''
        user = self.get_object()
        return (self.request.user.profile == user.profile)