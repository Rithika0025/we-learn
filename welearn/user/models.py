from django.db import models

# Create your models here.
class Student(models.Model):
    student_firstname = models.CharField(max_length=30)
    student_lastname = models.CharField(max_length=30)
    student_mother = models.CharField(max_length=30)
    student_father = models.CharField(max_length=30)
    student_address = models.CharField(max_length=100)
    student_gender = models.CharField(max_length=30)
    student_dob = models.DateField()
    student_pincode = models.IntegerField()
    student_qualification = models.CharField(max_length=100)
    student_email = models.CharField(max_length=30)
    student_password = models.CharField(max_length=50,default='')
    
class meta:
    db_table = 'student'