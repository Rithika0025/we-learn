from django.shortcuts import render

# Create your views here.
def student_master(request):
    return render(request,'student/student_master.html')

def student_home(request):
    return render(request,'student/student_home.html')
