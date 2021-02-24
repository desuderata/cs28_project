"""Django page views.

todo:
- change index to render instead of HttpResponse

author: Yee Hou, Teoh (2471020t)
        Ekaterina Terzieva(2403606t)
        # add yr name here if you are working on this file.
        Kien Welch 2371692w
        Alana Grant 239048G
"""
from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from django.http import HttpResponse

import re
import logging
from .models.academic_plan import AcademicPlan
from .models.graduation_year import GraduationYear

from .models.grade import Grade
from .models.student import Student
from django.contrib import messages



def index(request):
    return render(request, 'index.html')

@login_required
def student_upload(request):
    if request.method == "GET":
        return render(request, 'student_upload.html',{})
        
    try:
        csv_file = request.FILES.getlist("csv_file")
        for file in csv_file:
            file_data = file.read().decode("utf-8")
            lines = re.split('\r|\n', file_data)[1:]
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
                    logging.getLogger("error_logger").error("Unable to upload file. "+repr(e))                    
                    pass



    except Exception as e:
        logging.getLogger("error_logger").error("Unable to upload file. "+repr(e))

    return redirect(reverse("cs28:student_upload"))


def user_login(request):
    if request.user.is_authenticated:
        return redirect(reverse('cs28:index'))
    if request.method == "POST":
        # get username and password then check if acc is valid
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(username=username, password=password)

        if user:
            if user.is_active:
                login(request, user)
                return redirect(reverse('cs28:index'))
            else:
                return HttpResponse("The account you entered is not valid.")

        else:
            # wrong details
            print(f"Invalid login details: {username}, {password}")
            return redirect(reverse('cs28:login'))
    else:
        return render(request, 'login.html')


@login_required
def user_logout(request):
    logout(request)
    return redirect(reverse('cs28:index'))


@login_required
def manage(request):
    ctx = {"student": Student.objects.all()}
    return render(request, 'manage.html', context=ctx)


@login_required
def module_grades(request):
    ctx = {"grade": Grade.objects.all()}
    return render(request, 'module_grades.html', context=ctx)
