""" Tests Award Override

- Tests if award is successfully overridden

author: Yee Hou, Teoh (2471020t)
"""
import json
from django.test import TestCase

from .test_setup import login, populate
from cs28.models import Student, AcademicPlan, GraduationYear, Grade


class AwardOverrideTest(TestCase):
    def setUp(self):
        login(self.client)
        populate(self)

    def test_updated_award(self):
        """
        Tests if award is successfully overridden
        """
        self.client.post("/cs28/manage/calculate/",
                         {'year': '19-20',
                          'plan': 'F100-2208'})

        students = Student.objects.get(matricNo="2456789")

        data = {"field": "award",
                "row": json.dumps({"field": "award",
                                   "id": "2456789",
                                   "award": "Fail",
                                   "oAward": "A1"})}

        self.client.post("/cs28/manage/update/", data)
        students = Student.objects.get(matricNo="2456789")
        new_award = students.updatedAward

        self.assertNotEquals("A1", new_award)
        self.assertEquals(new_award, "Fail")
