"""Django page views.

author: Yee Hou, Teoh (2471020t)
        Ekaterina Terzieva(2403606t)
        Nguyen Thanh Hieu (2401707n)
        # add yr name here if you are working on this file.
        Kien Welch 2371692w
        Alana Grant 239048G
"""
import numpy as np
import json
import time

from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from django.http import HttpResponse, JsonResponse
from decimal import localcontext, Decimal, ROUND_HALF_UP
from django.contrib.admin.views.decorators import staff_member_required

from .convert_to_ttpt import to_ttpt
from cs28.models import Student, Grade, GraduationYear, AcademicPlan

import re
import logging
from .models.academic_plan import AcademicPlan
from .models.graduation_year import GraduationYear

from .models.grade import Grade
from .models.student import Student
from django.contrib import messages
import csv

import hashlib
from django.db.models.query_utils import Q


def _check_year(year):
    try:
        year1, year2 = year.split("-")
        return (int(year2) - int(year1) == 1) and \
            (len(year1) == 2) and \
            (len(year2) == 2)
    except Exception:
        return False


def _anonymize(matric):
    return hashlib.sha1(str(matric).encode("UTF-8")).hexdigest()[:11]


@login_required
def index(request):
    return render(request, 'index.html')


@login_required
def student_upload(request):
    if request.method == "GET":
        return render(request, 'student_upload.html', {})

    try:
        csv_file = request.FILES.getlist("file")
        for file in csv_file:
            success = True
            if not file.name.endswith('.csv'):
                print("File is not CSV type")
                error = "File is not CSV type"
                return JsonResponse({'error': error}, status=400)

            file_data = file.read().decode("utf-8")
            lines = re.split('\r\n|\r|\n', file_data)[1:]
            for line in lines:

                fields = line.split(",")
                try:
                    print(fields)
                    matricNo = fields[0]
                    givenNames = fields[1][1:]
                    surname = fields[2][:-1]
                    academicPlan = AcademicPlan.objects.get(planCode=fields[3])
                    gradYear = GraduationYear.objects.get(gradYear=fields[4])

                    Student.objects.get_or_create(

                        matricNo=matricNo,
                        givenNames=givenNames,
                        surname=surname,
                        academicPlan=academicPlan,
                        gradYear=gradYear,
                    )

                except Exception as e:
                    success = False
                    messages.error(request, "[" + line + "] " + str(e))
                    logging.getLogger("error_logger").error(
                        "Unable to upload file. " + repr(e))
                    error = str(e)
                    return JsonResponse({'error': error}, status=400)
                    pass

            if (success):
                messages.success(request, "All grades from file " +
                                 file.name + " were uploaded successfully!")
            else:
                messages.warning(request, "File " + file.name +
                                 " uploaded, but not all grades were uploaded successfully. Please check the error messages above.")
            time.sleep(1)

    except Exception as e:
        messages.error(request, e)
        logging.getLogger("error_logger").error(
            "Unable to upload file. "+repr(e))

        error = str(e)
        return JsonResponse({'error': error}, status=400)

    return redirect(reverse("cs28:student_upload"))


def user_login(request):
    if request.user.is_authenticated:
        return redirect(reverse('cs28:index'))
    if request.method == "POST":
        # get username and password then check if acc is valid
        username = request.POST.get("username")
        password = request.POST.get("password")
        remember_me = request.POST.get("remember") == "remember"

        user = authenticate(username=username,
                            password=password,
                            request=request)
        if not remember_me:
            request.session.set_expiry(0)

        if user:
            if user.is_active:
                login(request, user)
                return redirect(reverse('cs28:index'))
            else:
                return HttpResponse("The account you entered is not valid.")

        else:
            # wrong details
            messages.error(request, "Invalid username or password")
            return redirect(reverse('cs28:login'))
    else:
        return render(request, 'login.html')


@login_required
def user_logout(request):
    logout(request)
    return redirect(reverse('cs28:index'))


@login_required
def manage(request):
    ctx = {"student": Student.objects.all(),
           "years": GraduationYear.objects.all().order_by('gradYear'),
           "plans": AcademicPlan.objects.all().order_by('planCode'), }
    return render(request, 'manage.html', context=ctx)


def is_discretionary(student):
    award = student.finalAward4
    if ((17 < award < 18) or
            (14 < award < 15) or
            (11 < award < 12) or
            (8 < award < 9)):
        return True
    return False


@login_required
def data(request):
    year = request.GET.get('year', None)
    plan = request.GET.get('plan', None)

    if not (year and plan):
        messages.error(request, "Error retrieving data")
        return HttpResponse(status=400)

    students = Student.objects.filter(gradYear=year,
                                      academicPlan=plan)
    # students = Student.objects.all()
    json_array = []

    for student in students:
        row = {}
        row["anon"] = _anonymize(student.matricNo)
        row["id"] = student.matricNo
        row["mcId"] = student.matricNo
        row["grad"] = student.gradYear.gradYear
        row["name"] = student.surname + "," + student.givenNames
        row["first"] = student.givenNames
        row["last"] = student.surname
        row["plan"] = student.academicPlan.planCode
        row["gpa4"] = str(student.finalAward4)
        row["gpa3"] = str(student.finalAward3)
        row["gpa2"] = str(student.finalAward2)
        row["gpa1"] = str(student.finalAward1)
        row["gpa"] = str(student.finalAward)
        row["oAward"] = student.award_as_mc()
        row["award"] = student.award_as_mc() if student.updatedAward == "-1"\
            else student.updatedAward
        row["mcAward"] = student.award_as_mc() if student.updatedAward == "-1"\
            else student.updatedAward
        row["notes"] = student.notes

        sub = []
        grades = student.grade_set.all()

        # courses in the student academic plan
        courses = [c for c in student.academicPlan.get_courses() if c]
        is_updated = False
        for course in courses:
            sub_row = {}
            if grades.filter(courseCode=course).exists():

                grade = grades.filter(courseCode=course)
                sub_row["gradeId"] = student.matricNo
                sub_row["code"] = grade.values('courseCode')[0]['courseCode']
                sub_row["subNotes"] = grade.values('notes')[0]['notes']

                alpha = grade.values('alphanum')[0]['alphanum']
                u_alpha = grade.values('updatedGrade')[0]['updatedGrade']
                is_updated = u_alpha != "-1" if not is_updated else is_updated

                grade = alpha if u_alpha == "-1" else u_alpha
                sub_row["oAlpha"] = alpha
                sub_row["alpha"] = grade
                sub_row["ttpt"] = to_ttpt(grade)
            else:
                sub_row["gradeId"] = student.matricNo
                sub_row["code"] = course
                sub_row["alpha"] = "-"
                sub_row["ttpt"] = "-"
                sub_row["subNotes"] = ""
            sub.append(sub_row)
        row["sub"] = sub

        if student.updatedAward != "-1":
            row["type"] = "Degree Overridden"
        elif is_updated and student.hasSpecialCode:
            row["type"] = "Course Grade Adjusted"
        elif student.isMissingGrades or student.hasSpecialCode:
            row["type"] = "Incomplete Course Assessment"
        elif is_discretionary(student):
            row["type"] = "Discretionary"
        else:
            row["type"] = "No Issues"

        json_array.append(row)

    return JsonResponse(json_array, safe=False)


@login_required
def module_grades(request):
    ctx = {"grade": Grade.objects.all()}
    return render(request, 'module_grades.html', context=ctx)


@login_required
def update_field(request):
    if request.method == "POST":

        field = request.POST.get('field', None)
        row = json.loads(request.POST.get('row', None))
        # old_value = request.POST.get('el', None)

        # Update grade or award
        if field == "notes" or field == "award":
            matric = row["id"]
            student = Student.objects.get(matricNo=matric)

            if field == "notes":
                student.notes = row["notes"]
                student.save()

            if field == "award":
                award = row["award"]
                o_award = row["oAward"]

                student.updatedAward = award if award != o_award else "-1"
                student.save()

        if field == "alpha" or field == "subNotes":
            # First seven chars of gradeId is matric Num
            matric = row["gradeId"][:7]
            code = row["code"]

            student = Student.objects.get(matricNo=matric)

            if Grade.objects.filter(matricNo=student, courseCode=code).exists():

                grade = Grade.objects.get(matricNo=student, courseCode=code)
                if field == "alpha":
                    alpha = row["alpha"]
                    o_alpha = row["oAlpha"]

                    grade.updatedGrade = alpha if alpha != o_alpha else "-1"
                    grade.save()
                if field == "subNotes":
                    grade.notes = row["subNotes"]
                    grade.save()
            else:
                if field == "alpha":
                    print(row['alpha'])
                    grade, created = Grade.objects.get_or_create(
                        matricNo=student, courseCode=code)
                    grade.alphanum = row["alpha"]
                    grade.save()

        data = {
            'Status': 'success'
        }
        return JsonResponse(data)
    return JsonResponse({'Status': "failure"})


@login_required
def calculate(request):
    if request.method == "POST":
        year = request.POST.get('year', None)
        plan = request.POST.get('plan', None)
        json_row = request.POST.get('row', None)
        update_sub = False

        if json_row:
            row = json.loads(json_row)
            update_sub = "gradeId" in row.keys()

        if not ((year and plan) or update_sub):
            return HttpResponse(status=400)

        if update_sub:
            matric = row["gradeId"][:7]
            students = Student.objects.filter(matricNo=matric,
                                              gradeDataUpdated=True)

        else:
            students = Student.objects.filter(gradeDataUpdated=True,
                                              gradYear=year,
                                              academicPlan=plan)

        # if len(request.data) > 0:
        #     students = Student.object.filter(gradeDataUpdated=True,
        #                                      gradYear__in=request.data)
        # else:
        #     students = Student.objects.filter(gradeDataUpdated=True)

        course_counts = {}
        course_weights = {}

        for student in students.iterator():
            academic_plan = student.academicPlan
            plan_code = academic_plan.planCode
            weights = academic_plan.get_weights()
            courses = academic_plan.get_courses()

            numerical_score = []
            weight_list = []

            # get number of courses
            if plan_code not in course_counts.keys():
                # remove none values to get num of courses
                course_counts[plan_code] = len([c for c in courses if c])

            course_count = course_counts[plan_code]
            # get weight for academic plan
            if plan_code not in course_weights.keys():
                course_weights[plan_code] = {
                    courses[i]: weights[i] for i in range(course_count)}

            grades = Grade.objects.filter(matricNo=student.matricNo)
            # check if a course is missing
            is_missing_grades = course_count != len(grades)
            has_special_code = False

            for grade in grades.iterator():
                o_grade = grade.get_alphanum_as_num()
                u_grade = grade.get_updated_as_num()

                score = o_grade if u_grade == "-1" else u_grade
                if grade.is_grade_a_special_code():
                    has_special_code = True
                    continue

                if grade.courseCode not in courses:
                    is_missing_grades = True
                    continue

                # dot of vec to get sum of all weighted scores

                numerical_score.append(score)
                weight_list.append(course_weights[plan_code][grade.courseCode])
                overall_points = np.dot(weight_list, numerical_score)

            # Rounding: quantize for half up rounding
            def round(flt, dec):
                return Decimal(str(flt)).quantize(Decimal(dec),
                                                  rounding=ROUND_HALF_UP)

            student.finalAward = round(overall_points, "0")
            student.finalAward1 = round(overall_points, "0.0")
            student.finalAward2 = round(overall_points, "0.00")
            student.finalAward3 = round(overall_points, "0.000")
            student.finalAward4 = round(overall_points, "0.0000")

            student.set_is_missing_grades(is_missing_grades)
            student.set_has_special_code(has_special_code)

        students.update(gradeDataUpdated=False)
        return HttpResponse(status=201)
    return HttpResponse(status=400)


@login_required
@staff_member_required
def upload_course_grades(request):
    if request.method == "GET":
        return render(request, 'upload_course_grades.html', {})

    try:
        files = request.FILES.getlist("file")
        # check if file is too large
        # if csv_file.multiple_chunks():
        #    return redirect(reverse("cs28:upload_course_grades"))

        for file in files:
            success = True
            if not file.name.endswith('.csv'):
                print("File is not CSV type")
                error = "File is not CSV type"
                return JsonResponse({'error': error}, status=400)
            # extract course code from the file name, for now hard-coded
            # (expected format: "Grade Roster CourseCode.csv")
            courseCode = file.name[13:-9]

            file_data = file.read().decode("utf-8")
            lines = re.split('\r\n|\r|\n', file_data)[1:]
            for line in lines:

                if line == '':
                    continue

                fields = re.split('",|,"', line)
                try:

                    matricNo = Student.objects.get(matricNo=fields[0])
                    alphanum = fields[2]
                    Grade.objects.get_or_create(
                        courseCode=courseCode,
                        matricNo=matricNo,
                        alphanum=alphanum,
                    )
                except Exception as e:
                    logging.getLogger("error_logger").error(
                        "Unable to upload file. " + repr(e))
                    error = "[" + line + "] " + str(e)
                    return JsonResponse({'error': error}, status=400)
                    pass

            time.sleep(1)

    except Exception as e:
        messages.error(request, e)
        logging.getLogger("error_logger").error(
            "Unable to upload file. "+repr(e))
        error = str(e)
        return JsonResponse({'error': error}, status=400)

    return redirect(reverse("cs28:upload_course_grades"))


@login_required
def help(request):
    return render(request, 'help.html')


@login_required
def search_results(request):
    """Search results view.

    Splits the query, iterates through it then filter results
    """
    if request.method == "GET":
        query = request.GET.get('search')
        submit_button = request.GET.get('submit')

        if query:
            student = Student.objects.all()
            words = query.split()

            for w in words:
                lookup_student = Q(matricNo__icontains=w) | \
                    Q(givenNames__icontains=w) | \
                    Q(surname__icontains=w) | \
                    Q(gradYear__gradYear__icontains=w) | \
                    Q(academicPlan__planCode__icontains=w)
                student = student.filter(lookup_student).distinct()
            ctx = {'students': student,
                   'submit_button': submit_button}
            return render(request, 'search_results.html', ctx)

    return render(request, 'search_results.html')


@login_required
def graph(request):
    ctx = {"years": GraduationYear.objects.all(),
           "plans": AcademicPlan.objects.all(), }
    return render(request, 'graph.html', context=ctx)


def locked_out(request):
    return render(request, 'lockout.html')


@login_required
def upload_academic_plan(request):
    if request.method == "GET":
        return render(request, 'upload_academic_plan.html')

    try:
        files = request.FILES.getlist("file")

        for file in files:

            if not file.name.endswith('.csv'):
                print("File is not CSV type")
                error = "File is not CSV type"
                return JsonResponse({'error': error}, status=400)

            try:
                year = file.name[-9:-4]
                if not _check_year(year):
                    return JsonResponse({'error': 'Invalid year format.'},
                                        status=400)

                decoded_file = file.read().decode('utf-8').splitlines()
                grad_year, g_created = GraduationYear.objects.get_or_create(
                    gradYear=year)
                file_data = csv.reader(decoded_file,
                                       quotechar='"',
                                       delimiter=',',
                                       quoting=csv.QUOTE_ALL,
                                       skipinitialspace=True)

                # check headers
                file_header = [i for i in next(file_data)]
                expected_header = ["Academic Plan Code",
                                   "Internal Course Code",
                                   "MyCampus Description"]

                courses = [f"Course {i}" for i in range(1, 41)]
                weights = [f"Weight {i}" for i in range(1, 41)]

                expected_header.extend([j for i in zip(courses, weights)
                                        for j in i])

                if file_header != expected_header:
                    error = 'Incorrect file headers. Please refer to the Help \
                        Page for the correct header format'
                    return JsonResponse({'error': error}, status=400)

            except Exception as e:
                error = str(e)
                return JsonResponse({'error': error}, status=400)
            for line in file_data:
                if line == '':
                    continue
                try:
                    # course name and weight only
                    courses = line[3:]
                    a_plan = AcademicPlan.objects
                    plan, p_created = a_plan.get_or_create(gradYear=grad_year,
                                                           planCode=line[0],
                                                           courseCode=line[1],
                                                           mcName=line[2])
                    i = 0

                    for c, w in zip(courses[::2], courses[1::2]):
                        i += 1
                        if c and w:
                            setattr(plan, f"course_{i}", c)
                            setattr(plan, f"weight_{i}", w)
                            plan.save()
                except Exception as e:
                    error = str(e)
                    return JsonResponse({'error': error}, status=400)
            time.sleep(1)
    except Exception as e:
        print(str(e))

    return redirect(reverse("cs28:upload_academic_plan"))
