# Generated by Django 4.1.4 on 2023-03-20 07:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='student_pincode',
            field=models.IntegerField(),
        ),
    ]
