from django.urls import path
from . import views

urlpatterns = [
    path('master',views.welearn_master,name='master'),
    path('home',views.welearn_home,name='home'),
    path('signup',views.welearn_signup,name='signup'),
]
