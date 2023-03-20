from django.urls import path
from . import views

urlpatterns = [
     path('student_master',views.student_master,name='student_master'),
     path('student_home',views.student_home,name='student_home'),
]