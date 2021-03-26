""" Tests calculation

author: Yee Hou, Teoh (2471020t)
"""
from django.test import TestCase
from django.urls import reverse
from decimal import Decimal

from .test_setup import login, populate
from cs28.models import Student


class CalculationTest(TestCase):
    def setUp(self):
        login(self)
        populate(self)

    def test_calculation(self):
        """
        Tests whether calculation is successful and correct
        """
        # Test success
        response = self.client.post('/cs28/manage/calculate/',
                                    {'year': '19-20',
                                     'plan': 'F100-2208'})
        self.assertEqual(response.status_code, 201)

        # Test correctness
        student = Student.objects.get(matricNo='2456789')
        self.assertEqual(student.finalAward4, Decimal('9.0240'))
