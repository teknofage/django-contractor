from django.urls import path
from accounts.views import SignUpView, LogInView, ProfileSetupView, HomeView

urlpatterns = [
    path('signup/', SignUpView.as_view(), name='signup'),
    path('login/', LogInView.as_view(), name='login'),
    path('login/profiles/home', ProfileSetupView.as_view(), name='profile-setup'),
    # path('login/profiles/submit', HomeView.as_view(), name='home-view'),
    path('login/profiles/submit/redirect', HomeView.as_view, name='home-view'),
]