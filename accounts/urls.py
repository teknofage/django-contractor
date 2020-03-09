from django.urls import path
from accounts.views import (
    SignUpView, 
    LogInView, 
    ProfileSetupView, 
    ProfileUpdateView, 
    HomeView, 
    logout_view
)


urlpatterns = [
    path('signup/', SignUpView.as_view(), name='signup'),
    path('login/', LogInView.as_view(), name='login'),
    path('login/profiles/home', ProfileSetupView.as_view(), name='profile-setup'),
    path('login/accounts/update', ProfileUpdateView.as_view(), name='profile-update'),
    path('login/profiles/submit/redirect', HomeView.as_view(), name='home-view'),
    path('login/profiles/redirect', HomeView.as_view(), name='show-home-view'),
    path('logout', logout_view, name='logout'),
]   