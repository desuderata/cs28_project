"""URLs for app

author: Yee Hou, Teoh (2471020t)
        Ekaterina Terzieva(2403606t)
        Nguyen Thanh Hieu(2401707n)
        # add yr name here if you are working on this file.
        Kien Welch 2371692w
"""
from django.urls import path
from cs28 import views

app_name = 'cs28'

urlpatterns = [
    path('', views.index, name='index'),
    # path('cs28', include('django.contrib.auth.urls')),
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),

    path('module-grades/', views.module_grades, name='module_grades'),
    path('course-grades/', views.module_grades, name='course_grades'),
    path('student-upload/', views.student_upload, name='student_upload'),
    path('module-grades-upload/', views.module_grades_upload,
         name='module_grades_upload'),

    path('manage/', views.manage, name='manage'),
    path('manage/calculate/', views.calculate, name='calculate'),
    path('manage/update/', views.update_field, name='update'),
    path('manage/data/', views.data, name='data'),

    path('help-page/', views.help, name='help_page'),
    path('search-results/', views.search_results, name="search_results"),
]
