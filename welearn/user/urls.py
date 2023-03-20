from django.urls import path
from . import views

urlpatterns = [
    path('master',views.welearn_master,name='master'),
    path('home',views.welearn_home,name='home'),
    path('studentsignup',views.welearn_studentsignup,name='studentsignup'),
    path('teachersignup',views.welearn_teachersignup,name='teachersignup'),
    path('teacherlogin',views.welearn_teacherlogin,name='teacherlogin'),
    path('studentlogin',views.welearn_studentlogin,name='studentlogin'),
]
