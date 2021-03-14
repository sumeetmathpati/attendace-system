from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class Class(models.Model):
    title = models.CharField(max_length=10)

class Student(models.Model):
    name = models.CharField(max_length=50)
    mac = models.CharField(max_length=17)
    email = models.EmailField()
    class_name = models.ForeignKey(Class, on_delete=models.SET_NULL, null=True)

class Record(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    present_time = models.DateTimeField(default=timezone.now)

