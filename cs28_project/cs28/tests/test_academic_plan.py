""" Tests Academic plans

- Tests if a change in course code results in a change in student grades
course code
- Tests if sum of course grades adds up correctly
- Tests if there is a duplicate course
- Tests whether the course has a corresponding weight to it
- Tests whether a weight has a corresponding weight to it

author: Yee Hou, Teoh (2471020t)
"""
from django.test import TestCase
from django.core.exceptions import ValidationError
from decimal import Decimal

from .test_setup import login, populate
from cs28.models import Student, AcademicPlan, GraduationYear, Grade


class AcademicPlanTest(TestCase):
    def setUp(self):
        populate(self)
        self.year = GraduationYear.objects.get(gradYear="19-20")

    def test_course_code_change_cascade(self):
        """
        Checks if a change in course code in academic plan cascades to
        student grades
        """
        academic_plan = AcademicPlan.objects.get(planCode="F100-2208")

        academic_plan.course_1 = "CHEM_9999"
        academic_plan.save()

        grade = Grade.objects.get(matricNo=self.student, alphanum="A1")
        self.assertNotEqual(grade.courseCode, "CHEM_3012")
        self.assertEqual(grade.courseCode, "CHEM_9999")

    def test_weight_sum(self):
        """
        Tests if sum of course grades adds up correctly
        """
        plan = AcademicPlan.objects

        # this should exist
        plan.create(gradYear=self.year,
                    planCode="Correct",
                    courseCode="Test",
                    mcName="Test",
                    course_1="Foobar", weight_1=0.5,
                    course_2="Barfoo", weight_2=0.5)

        # this should not exist
        with self.assertRaises(ValidationError):
            plan.create(gradYear=self.year,
                        planCode="Wrong",
                        courseCode="Test",
                        mcName="Test",
                        course_1="Foobar", weight_1=0.5,
                        course_2="Barfoo", weight_2=0.6).clean()

        self.assertTrue(plan.filter(planCode="Correct").exists())
        self.assertFalse(plan.filter(planCode="Wrong").exists())

    def test_duplicate_course(self):
        """
        Tests if there is a duplicate course
        """
        plan = AcademicPlan.objects.create(gradYear=self.year,
                                           planCode="Foobar",
                                           courseCode="Foobar",
                                           mcName="Foobar",
                                           course_1="Foobar", weight_1=0.5,
                                           course_2="Foobar", weight_2=0.5)
        with self.assertRaises(ValidationError):
            plan.clean()

    def test_corresponding_weight_exists(self):
        """
        Tests whether the course has a corresponding weight to it
        """
        with self.assertRaises(ValidationError):
            AcademicPlan.objects.create(gradYear=self.year,
                                        planCode="Foobar",
                                        courseCode="Foobar",
                                        mcName="Foobar",
                                        course_1="Foobar", weight_1=0.5,
                                        course_2="Foobar")

    def test_corresponding_course_exists(self):
        """
        Tests whether a weight has a corresponding weight to it
        """
        with self.assertRaises(ValidationError):
            AcademicPlan.objects.create(gradYear=self.year,
                                        planCode="Foobar",
                                        courseCode="Foobar",
                                        mcName="Foobar",
                                        course_1="Foobar", weight_1=0.5,
                                        weight_2=0.5)

    def test___str__(self):
        """
        Tests if to string works as intended
        """
        plan = AcademicPlan.objects.get(planCode="F100-2208")
        self.assertTrue(str(plan), "F100-2208")
