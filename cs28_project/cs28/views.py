"""Django page views.

todo:
- change index to render instead of HttpResponse

author: Yee Hou, Teoh (2471020t)
        Ekaterina Terzieva(2403606t)
        Nguyen Thanh Hieu (2401707n)
        # add yr name here if you are working on this file.
        Kien Welch 2371692w
"""
from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from django.http import HttpResponse

import logging
from .models.grade import Grade
from .models.student import Student
from django.contrib import messages


def index(request):
    return render(request, 'index.html')


def studentUpload(request):
    return render(request, 'studentUpload.html')


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
    return render(request, 'manage.html')


@login_required
def module_grades(request):
    return render(request, 'module_grades.html')

@login_required
def module_grades_upload(request):
    if request.method == "GET":
        return render(request, 'module_grades_upload.html', {})
    
    try:
        csv_file = request.FILES["csv_file"]
        if not csv_file.name.endswith('.csv'):
            messages.error(request,"File is not CSV type")
            return redirect(reverse("cs28:module_grades_upload"))
        #check if file is too large
        if csv_file.multiple_chunks():
            return redirect(reverse("cs28:module_grades_upload"))
        
        file_data = csv_file.read().decode("utf-8")
        
        lines = file_data.split("\r")
        lines.remove(lines[0])
        for line in lines:
            fields = line.split(",")
            print (fields)
            try:
                courseCode = csv_file.name
                #extract course code from the file name, for now hard-coded (expected format: "Grade Roster CourseCode.csv")
                courseCode = courseCode[13:-4]
                print(courseCode)
                matricNo = Student.objects.get(matricNo = fields[0])
                alphanum = fields[2]
                Grade.objects.create(
                    courseCode = courseCode,
                    matricNo = matricNo,
                    alphanum = alphanum,
                )                                           
            except Exception as e:
                logging.getLogger("error_logger").error("Unable to upload file. "+repr(e))                    
                pass


    except Exception as e:
        logging.getLogger("error_logger").error("Unable to upload file. "+repr(e))

    return redirect(reverse("cs28:module_grades_upload"))
