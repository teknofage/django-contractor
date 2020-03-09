from django.shortcuts import render
from django.views.generic import TemplateView

class SplashView(TemplateView):
    template_name = 'splash.html'
    success_url = 'splash.html'
    # success_url = 'registration/signup.html'
    
    def get(self, request):
        return render(request, self.template_name)