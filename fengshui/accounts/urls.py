from django.urls import path
from accounts.views import SignUpView, LogInView, ProfileHomeView, HomeView

urlpatterns = [
    path('signup/', SignUpView.as_view(), name='signup'),
    path('login/', LogInView.as_view(), name='login'),
    path('login/profiles/home', ProfileHomeView.as_view(), name='profile-home'),
    path('login/profiles/submit', HomeView.as_view(), name='home-view'),
    path('login/profiles/submit/redirect', HomeView.as_view, name='home-view'),
]