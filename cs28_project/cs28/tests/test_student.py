""" Test Student

- Tests for matriculation number validation
- Tests if unset_grade_data_updated() works
- Tests if award_as_mc returns the correct mc award
- Tests if to string works as intended

author: Yee Hou, Teoh (2471020t)
"""
from django.test import TestCase
from django.core.exceptions import ValidationError

from .test_setup import login, populate
from cs28.models import Student, Grade, AcademicPlan, GraduationYear
from decimal import Decimal


def _create_student(matric):
    year_19_20 = GraduationYear.objects.get(gradYear="19-20")
    plan = AcademicPlan.objects.get(planCode="F100-2208")
    return Student.objects.get_or_create(matricNo=matric,
                                         givenNames="test",
                                         surname="student",
                                         academicPlan=plan,
                                         gradYear=year_19_20)


class StudentTest(TestCase):
    def setUp(self):
        login(self.client)
        populate(self)

    def test_wrong_matriculation_number(self):
        """
        Tests for matriculation number validation
        """
        with self.assertRaises(ValidationError):
            _create_student("invalid")

    def test_unset_grade_data(self):
        """
        Tests if unset_grade_data_updated() works
        """
        self.student.set_grade_data_updated()
        self.student.unset_grade_data_updated()
        self.assertFalse(self.student.gradeDataUpdated)

    def test_return_award_as_mc(self):
        """
        Tests if award_as_mc returns the correct mc award
        """
        self.student.finalAward4 = Decimal(str("0.0000"))
        self.assertEquals(self.student.award_as_mc(), "Fail")

        self.student.finalAward4 = Decimal(str("9.0000"))
        self.assertEquals(self.student.award_as_mc(), "33")

        self.student.finalAward4 = Decimal(str("12.0000"))
        self.assertEquals(self.student.award_as_mc(), "0L")

        self.student.finalAward4 = Decimal(str("15.0000"))
        self.assertEquals(self.student.award_as_mc(), "0U")

        self.student.finalAward4 = Decimal(str("18.0000"))
        self.assertEquals(self.student.award_as_mc(), "01")

    def test___str__(self):
        """
        Tests if to string works as intended
        """
        student = Student.objects.get(matricNo="2456789")
        self.assertTrue(str(student), "2456789 (Pooper, Party)")
