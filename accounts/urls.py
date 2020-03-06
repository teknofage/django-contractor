from django.urls import path
from accounts.views import SignUpView, LogInView, ProfileSetupView, HomeView, UserDelete

urlpatterns = [
    path('signup/', SignUpView.as_view(), name='signup'),
    path('login/', LogInView.as_view(), name='login'),
    path('login/profiles/home', ProfileSetupView.as_view(), name='profile-setup'),
    # path('login/profiles/submit', HomeView.as_view(), name='home-view'),
    path('<int:pk>/profiles/home', HomeView.as_view(), name='home-view'),
    
    path('<int:pk>/profile/', ProfileSetupView.as_view(), name='acct_info'),
    # path('<int:pk>/change-account-details/', AccountUpdate.as_view(), name='change-info'),
    path('<int:pk>/delete-account/', UserDelete.as_view(), name='delete_account'),
]