from django.urls import path
from accounts.views import SignUpView, LogInView, ProfileHomeView

urlpatterns = [
    path('signup/', SignUpView.as_view(), name='signup'),
    path('login/', LogInView.as_view(), name='login'),
    path('login/profiles/home', ProfileHomeView.as_view(), name='profile-home')
]