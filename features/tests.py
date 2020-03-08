import unittest

from django.test import TestCase, Client, SimpleTestCase
from django.contrib.auth.models import User
from .models import Direction
from accounts.models import Profile
from django.urls import reverse
# Create your tests here.

class HomePageTests(SimpleTestCase, Profile):
    
    def test_home_page_status_code(self):
        response = self.client.get('/accounts/login')
        self.assertEquals(response.status_code, 301)
        
    def test_login_view_url_by_name(self):
        response = self.client.get(reverse('login'))
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'registration/login.html')
        
    def test_signup_view_url_by_name(self):
        response = self.client.get(reverse('signup'))
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'registration/signup.html')
        
    def test_home_view_uses_correct_template(self):
        response = self.client.get(reverse('home-view'))
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'home-view.html')