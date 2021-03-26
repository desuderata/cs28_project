""" Tests Graduation Year

- Tests if graduation year validator works
- Tests if to string works as intended

author: Yee Hou, Teoh (2471020t)
"""
from django.test import TestCase
from django.core.exceptions import ValidationError

from .test_setup import login, populate
from cs28.models import GraduationYear


class GraduationYearOverride(TestCase):
    def setUp(self):
        login(self)
        populate(self)

    def test_grad_year_validator(self):
        """
        Tests if graduation year validator works
        """
        year = GraduationYear.objects
        year.create(gradYear="20-22")

        with self.assertRaises(ValidationError):
            invalid = year.get(gradYear="20-22")
            invalid.full_clean()

    def test___str__(self):
        """
        Tests if to string works as intended
        """
        year = GraduationYear.objects.get(gradYear="19-20")
        self.assertTrue(str(year), "19-20")
