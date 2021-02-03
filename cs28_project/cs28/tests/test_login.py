"""Test for login

Tests for the following functionalities:
- User creation
- User login
- Redirect user to home after login

author: Yee Hou, Teoh (2471020t)
"""

from django.contrib.auth.models import User
from django.test import TestCase
from django.urls import reverse


class LoginTest(TestCase):
    def setUp(self):
        """
        Setup by creates a user
        """
        self.user, created = User.objects.get_or_create(username='testuser',
                                                        first_name='Test',
                                                        last_name='User',
                                                        email='test@test.com')
        self.user.set_password('password')
        self.user.save()
        self.assertTrue(created, "User was not created.")

    def test_login(self):
        # log user in
        response = self.client.post(reverse('cs28:login'),
                                    {'username': 'testuser',
                                     'password': 'password'})
        try:
            self.assertEqual(self.user.id,
                             int(self.client.session['_auth_user_id']),
                             "Wrong user logged in"
                             "Perhaps a different user was logged in?")
        except KeyError:
            self.assertTrue(False, "Login failed.")

        self.assertEqual(response.url, reverse('cs28:index'),
                         "User was not redirected to home page after login")
