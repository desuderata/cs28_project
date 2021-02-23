""" Tests Grades

author: Yee Hou, Teoh (2471020t)
"""
from django.test import TestCase
from django.core.exceptions import ValidationError

from .test_setup import login, populate
from cs28.models import Student, Grade


class GradesTest(TestCase):
    def setUp(self):
        login(self.client)
        populate(self)
        self.grade = Grade.objects.get(courseCode="CHEM_4012",
                                       matricNo=self.student)

    def test_grade_data_updated(self):
        grade = Grade.objects.get(courseCode="CHEM_4012",
                                  matricNo=self.student)
        old_grade = grade.alphanum

        grade.alphanum = "A1"
        grade.save()

        self.assertFalse(grade.alphanum == old_grade)
        self.assertTrue(self.student.gradeDataUpdated)

    def test_course_does_not_exist(self):
        """
        Checks if the course for the grade added exists. If it doesn't
        the course should not be created.
        """

        with self.assertRaises(ValidationError):
            grade = Grade.objects.get_or_create(courseCode="DNE",
                                                matricNo=self.student,
                                                alphanum="A1")
            grade.save()

        self.assertFalse(Grade.objects.filter(courseCode="DNE").exists())

    def test_is_special_code(self):
        """
        Tests if there is a special course in a student's grade
        """
        grade = Grade.objects.get(courseCode="CHEM_4012",
                                  matricNo=self.student)
        grade.alphanum = "MV"

        self.assertTrue(grade.is_grade_a_special_code)

    def test_delete_grade(self):
        """
        Tests if a course does not exist after it has been deleted
        """
        self.grade.delete()
        self.assertFalse(Grade.objects.filter(courseCode="CHEM_4012").exists())

    def test___str__(self):
        self.assertEqual(str(self.grade), "2456789 : CHEM_4012 F1")
