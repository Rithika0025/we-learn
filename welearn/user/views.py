from django.shortcuts import render,redirect
from user.models import Student

# Create your views here.
def welearn_master(request):
    return render(request,'user/master.html')

def welearn_home(request):
    return render(request,'user/home.html')

def welearn_studentsignup(request):
    if request.method == 'POST':
        first_name = request.POST['s_firstname']
        last_name = request.POST['s_lastname']
        mother_name = request.POST['s_mothername']
        father_name = request.POST['s_fathername']
        address = request.POST['s_address']
        gender = request.POST['s_gender']
        dob = request.POST['s_dob']
        pincode = request.POST['s_pincode']
        qualifications = request.POST['s_qualification']
        email_id = request.POST['s_email']
        
        student1 = Student(
            student_firstname = first_name,
            student_lastname = last_name,
            student_mother = mother_name,
            student_father = father_name,
            student_address = address,
            student_gender = gender,
            student_dob = dob,
            student_pincode = pincode,
            student_qualification = qualifications,
            student_email = email_id
        )
        student1.save()
        return redirect('user:student_home')
    return render(request,'user/student_signup.html')

def welearn_teachersignup(request):
    return render(request,'user/teacher_signup.html')

def welearn_teacherlogin(request):
    return render(request,'user/teacher_login.html')

def welearn_studentlogin(request):
    msg=''
    if request.method == 'POST':
        email = request.POST ['s_email']
        password = request.POST['s_password']
        try:
            student =Student.objects.get(
                student_email = email ,
                student_password = password
            )
            request.session['student'] = student.id
            return redirect ('student:student_login')
        except:
            msg = "Invalid email or password"
    return render(request,'user/student_login.html')

