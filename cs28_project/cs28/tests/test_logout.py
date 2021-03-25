"""Test for logout

Tests for the following functionalities:
- User creation
- User logout

author: Yee Hou, Teoh (2471020t)
"""

from django.contrib.auth.models import User
from django.test import TestCase
from django.urls import reverse
from .test_setup import user_create


class LogoutTest(TestCase):
    def setUp(self):
        """
        Setup by creates a user
        """
        self.user, created = user_create()
        self.assertTrue(created, "User was not created.")

    def test_logout(self):
        """
        Tests whether a user that is logged in can log out.
        """
        # log user in for testing
        with self.settings(AXES_ENABLED=False):
            self.client.login(username='testuser', password='password')
        try:
            self.assertEqual(self.user.id,
                             int(self.client.session['_auth_user_id']),
                             "Wrong user logged in")
        except KeyError:
            self.assertTrue(False, "Login failed.")

        # test logout
        response = self.client.get(reverse('cs28:logout'))
        self.assertEqual(response.status_code, 302,
                         "A redirect was expected. "
                         "User should be redirected when logging out")
        self.assertTrue('_auth_user_id' not in self.client.session,
                        "Logout did not log users out")
