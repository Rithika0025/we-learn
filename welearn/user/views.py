from django.shortcuts import render

# Create your views here.
def welearn_master(request):
    return render(request,'user/master.html')
def welearn_home(request):
    return render(request,'user/home.html')
def welearn_signup(request):
    return render(request,'user/signup.html')
