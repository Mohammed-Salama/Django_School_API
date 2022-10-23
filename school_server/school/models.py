# models.py
import email
from django.db import models

class Parent(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    address = models.TextField()
    phone_number = models.CharField(max_length=50)

    def __str__(self):
        return self.first_name+" "+self.last_name

    class Meta:
        db_table = 'parent'

class Student(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    school_class = models.IntegerField()
    age = models.IntegerField()
    parent = models.ForeignKey(Parent,related_name='student', on_delete=models.CASCADE)
    def __str__(self):
        return self.first_name+" "+self.last_name
    
    class Meta:
        db_table = 'student'

class Subject(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()
    students = models.ManyToManyField(Student,related_name='subjects')
    
    def __str__(self):
        return self.name

    class Meta:
        db_table = 'subject'
