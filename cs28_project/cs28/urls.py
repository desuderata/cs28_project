"""URLs for app

author: Yee Hou, Teoh (2471020t)
        Ekaterina Terzieva(2403606t)
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
    path('manage/', views.manage, name='manage'),
    path('course_grades/', views.module_grades, name='course_grades'),
    path('studentUpload/', views.studentUpload, name='studentUpload'),
    path('calculate/', views.calculate, name='calculate'),
    path('update/', views.update_field, name='update')
]
