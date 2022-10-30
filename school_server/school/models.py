# models.py
from django.db import models

class User(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    address = models.TextField()
    phone_number = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    school_class = models.IntegerField(null=True, blank=True)
    age = models.IntegerField()
    parent = models.ForeignKey('self',related_name='student', on_delete=models.CASCADE , null=True , blank=True)
    mark = models.IntegerField(null = True , blank = True)
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    type = models.CharField(max_length=50)

    def __str__(self):
        return self.first_name+" "+self.last_name

    class Meta:
        db_table = 'user'
        constraints=[
			models.CheckConstraint(check= models.Q(first_name__gte='A' ) & models.Q(first_name__lte='Z') , name='first_name_uppercase'),
            models.CheckConstraint(check= models.Q(last_name__gte='A' ) & models.Q(last_name__lte='Z') , name='last_name_uppercase'),
		]

        

class Subject(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()
    students = models.ManyToManyField(User,related_name='subjects',null = True , blank = True)
    
    def __str__(self):
        return self.name

    class Meta:
        db_table = 'subject'

class Token(models.Model):
    token = models.CharField(max_length=50)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    def __str__(self):
        return self.token

    class Meta:
        db_table = 'token'