from django.contrib.auth.models import User
from django.test import TestCase, Client
from .models import Profile
# Create your tests here.

class UserTestCase(TestCase):
    def setUp(self):
        Profile.objects.create(name="Judd", zodiac_animal="Ox", date_of_birth=12/12/1999, gender="M", direction="South")
        
    def test_profile_setup(self):
        judd = Profile.objects.get(name="Judd")
        
        self.assertEqual(judd.name == "Judd")
        

class UserTestCase(TestCase):
    def test_true_is_true(self):
        self.assertEqual(True, True)
    
    
class SearchFormTestCase(TestCase):
    def test_empty_get(self):
        response = self.client.get('/', HTTP_HOST='localhost')
        self.assertEqual(response.status_code, 400)
        

class CreateUserTest(TestCase):
    """ Test if User works """
    def setUp(self):
        self.user = User.objects.create(username='testuser')
        self.user.set_password('12345')
        self.user.save()
        self.c = Client()
        self.logged_in = self.c.login(username='testuser', password='12345')
    
    def test_user_login(self):
        """ Test if user is logged in"""
        self.assertTrue(self.logged_in)

    def test_login_credential(self):
        """ Test if user has the right credentials """
        self.assertEqual(self.user.username, 'testuser')
        self.assertEqual(self.user.password, '12345')