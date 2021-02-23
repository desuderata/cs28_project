"""Population script

author: Yee Hou, Teoh (2471020t)
"""

import os
import django
import random
import csv

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'cs28_project.settings')
django.setup()

from django.contrib.auth.models import User
from cs28.models import GraduationYear, AcademicPlan, Student, Grade


def populate_users():
    # Admin user
    admin, _ = User.objects.get_or_create(username="admin",
                                          email="admin@a.a")
    admin.is_staff = True
    admin.is_superuser = True
    admin.save()

    admin.set_password("password")
    admin.save()
    print("Created superuser...")

    # Staff user
    staff, _ = User.objects.get_or_create(username="staff",
                                          email="staff@a.a")
    staff.is_staff = True
    staff.save()

    staff.set_password("password")
    staff.save()
    print("Created staff user...")

    # Normal user
    user, _ = User.objects.get_or_create(username="user",
                                         email="user@a.a")
    user.save()

    user.set_password("password")
    user.save()
    print("Created normal user...")


def populate_graduation_year():
    GraduationYear.objects.get_or_create(gradYear="15-16")
    GraduationYear.objects.get_or_create(gradYear="16-17")
    GraduationYear.objects.get_or_create(gradYear="17-18")
    GraduationYear.objects.get_or_create(gradYear="18-19")
    GraduationYear.objects.get_or_create(gradYear="19-20")
    GraduationYear.objects.get_or_create(gradYear="20-21")
    print("Populated graduation year...")


def populate_academic_plan():
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
    year_20_21 = GraduationYear.objects.get(gradYear="20-21")
    AcademicPlan.objects.get_or_create(gradYear=year_20_21,
                                       planCode="F101-2207",
                                       courseCode="CHEM-5M",
                                       mcName="Chemistry with WP,MSci",
                                       course_1="CHEM_4012", weight_1=0.057,  # Org 3
                                       course_2="CHEM_4009", weight_2=0.057,  # Inorg 3
                                       course_3="CHEM_4014", weight_3=0.057,  # Phys 3
                                       course_4="CHEM_5016", weight_4=0.029,  # Front 3
                                       course_5="CHEM_4025", weight_5=0.200,  # Placement
                                       course_6="CHEM_5009P", weight_6=0.171,  # Project
                                       course_7="CHEM_5022", weight_7=0.086,  # Phys 4
                                       course_8="CHEM_5021", weight_8=0.086,  # Org 4
                                       course_9="CHEM_5017", weight_9=0.086,  # Inorg 4
                                       course_10="CHEM_5003", weight_10=0.086,  # ST
                                       course_11="CHEM_5005", weight_11=0.086,  # Prob
                                       )
    print("Populate Academic plans...")


def populate_students():
    with open("population_csv/student.csv") as f:
        reader = csv.reader(f)
        next(reader)  # skip header
        notes = ["The quick brown fox", "jumps over the lazy dog",
                 "Lorem ipsum dolor sit amet, consectetur adipiscing elit",
                 "sed do eiusmod tempor incididunt ut labore",
                 "et dolore magna aliqua.", "Ut enim ad minim veniam",
                 "quis nostrud exercitation ullamco laboris nisi ut aliquip",
                 "ex ea commodo consequat. Duis aute irure dolor",
                 "in reprehenderit in voluptate velit esse cillum dolore",
                 "eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat",
                 "non proident, sunt in culpa qui officia deserunt",
                 "mollit anim id est laborum."]

        for row in reader:
            rand_award = round(random.uniform(0, 22), 4)
            first, last = row[1].split(",")
            plan = AcademicPlan.objects.get(planCode=row[2])
            year = GraduationYear.objects.get(gradYear=row[3])
            note = random.choice([random.choice(notes), ""])
            Student.objects.get_or_create(matricNo=row[0],
                                          givenNames=last,
                                          surname=first,
                                          academicPlan=plan,
                                          gradYear=year,
                                          finalAward4=rand_award,
                                          notes=note)
    print("Populated students...")


def populate_grades():
    with open("population_csv/student.csv") as f:
        reader = csv.reader(f)
        next(reader)  # skip header

        grades = ["A1", "A2", "A3", "A4", "A5",
                  "B1", "B2", "B3", "C1", "C2",
                  "C3", "D1", "D2", "D3", "E1",
                  "E2", "E3", "F1", "F2", "F3",
                  "G1", "G2", "H", "CW", "CR", "MV"]
        courses = {"F100-2208": ["CHEM_3012", "CHEM_3009", "CHEM_3014",
                                 "CHEM_4003P", "CHEM_4014", "CHEM_4012",
                                 "CHEM_4009", "CHEM_4001"],
                   "F101-2207": ["CHEM_4012", "CHEM_4009", "CHEM_4014",
                                 "CHEM_5016", "CHEM_4025", "CHEM_5009P",
                                 "CHEM_5022", "CHEM_5021", "CHEM_5017",
                                 "CHEM_5003", "CHEM_5005"]}

        for row in reader:
            matric_no = Student.objects.get(matricNo=row[0])

            for i in range(len(courses[row[2]])):
                Grade.objects.get_or_create(courseCode=courses[row[2]][i],
                                             matricNo=matric_no,
                                             alphanum=random.choice(grades))
    print("Populated Grades...")


def populate():
    populate_users()
    populate_graduation_year()
    populate_academic_plan()
    populate_students()
    populate_grades()


if __name__ == '__main__':
    print("Populating cs28 database")
    populate()
