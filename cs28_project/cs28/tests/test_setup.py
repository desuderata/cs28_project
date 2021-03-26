""" Helper functions to setup

author: Yee Hou, Teoh (2471020t)
"""
from django.contrib.auth.models import User
from cs28.models import AcademicPlan, GraduationYear, Student, Grade


def user_create():
    """
    Creates a user

    Returns:
        Returns a tuple user, created where user is the created user
        and create is a boolean value; true when created and false when
        it isn't
    """
    user, created = User.objects.get_or_create(username='testuser',
                                               first_name='Test',
                                               last_name='User',
                                               email='test@test.com')
    user.set_password('password')
    user.save()

    return (user, created,)


def login(self):
    """
    Creates user and logs them in

    Args:
        client: the client to log in to
    """

    with self.settings(AXES_ENABLED=False):
        client = self.client
        user_create()
        client.login(username='testuser', password='password')


def populate(self):
    """
    Sets up the test db
    """
    GraduationYear.objects.get_or_create(gradYear="19-20")

    year_19_20 = GraduationYear.objects.get(gradYear="19-20")
    AcademicPlan.objects.get_or_create(gradYear=year_19_20,
                                       planCode="F100-2208",
                                       courseCode="CHEM-4H",
                                       mcName="Chemistry, BSc",
                                       course_1="CHEM_3012", weight_1=0.083,
                                       course_2="CHEM_3009", weight_2=0.083,
                                       course_3="CHEM_3014", weight_3=0.083,
                                       course_4="CHEM_4003P", weight_4=0.25,
                                       course_5="CHEM_4014", weight_5=0.125,
                                       course_6="CHEM_4012", weight_6=0.125,
                                       course_7="CHEM_4009", weight_7=0.125,
                                       course_8="CHEM_4001", weight_8=0.125,
                                       )

    plan = AcademicPlan.objects.get(planCode="F100-2208")
    Student.objects.get_or_create(matricNo="2456789",
                                  givenNames="Party",
                                  surname="Pooper",
                                  academicPlan=plan,
                                  gradYear=year_19_20)

    student = Student.objects.get(matricNo="2456789")
    Grade.objects.get_or_create(courseCode="CHEM_3012",
                                matricNo=student,
                                alphanum="A1")
    Grade.objects.get_or_create(courseCode="CHEM_3009",
                                matricNo=student,
                                alphanum="B1")
    Grade.objects.get_or_create(courseCode="CHEM_3014",
                                matricNo=student,
                                alphanum="C1")
    Grade.objects.get_or_create(courseCode="CHEM_4003P",
                                matricNo=student,
                                alphanum="D1")
    Grade.objects.get_or_create(courseCode="CHEM_4014",
                                matricNo=student,
                                alphanum="E1")
    Grade.objects.get_or_create(courseCode="CHEM_4012",
                                matricNo=student,
                                alphanum="F1")
    Grade.objects.get_or_create(courseCode="CHEM_4009",
                                matricNo=student,
                                alphanum="G1")
    Grade.objects.get_or_create(courseCode="CHEM_4001",
                                matricNo=student,
                                alphanum="H")
    student.gradeDataUpdated = True
    student.save()
    self.student = student
