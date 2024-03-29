# Generated by Django 4.1.4 on 2023-03-19 19:02

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('student_firstname', models.CharField(max_length=30)),
                ('student_lastname', models.CharField(max_length=30)),
                ('student_mother', models.CharField(max_length=30)),
                ('student_father', models.CharField(max_length=30)),
                ('student_address', models.CharField(max_length=100)),
                ('student_gender', models.CharField(max_length=30)),
                ('student_dob', models.DateField()),
                ('student_pincode', models.IntegerField(max_length=30)),
                ('student_qualification', models.CharField(max_length=100)),
                ('student_email', models.CharField(max_length=30)),
            ],
        ),
    ]
