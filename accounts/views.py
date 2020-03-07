from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from .forms import ProfileSetupForm
from django.urls import reverse_lazy, reverse
from django.views.generic import CreateView, TemplateView
from django.http import HttpResponseRedirect
from .models import Profile

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
        # if form.
        pass
    
class HomeView(TemplateView):
    template_name = 'home-view.html'

    def get(self, request, *args, **kwargs):
        current_user = request.user
        profile_data = Profile.objects.get(user=current_user)
        
        return render(request, 'home-view.html', {'profile':profile_data})
    
    


    
    # def get_context_data(self, **kwargs):
    #     user = self.queryset.get(id=pk)
    #     profile = user.profile
    #     # user = Profile.objects.get(Profile.zodiac_animal, Profile.date_of_birth, Profile.gender)
    #     context = super().get_context_data(**kwargs)
    #     context["form"] = {"zodiac_animal": user.zodiac_animal, "date_of_birth": "asdf", "gender":"asd"}
    #     return context
    
        