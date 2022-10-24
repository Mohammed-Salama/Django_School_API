from django.http import JsonResponse
from django.views import View
from django.core import serializers
from school.models import Student as StudentModel
from school.models import Parent as ParentModel
from school.models import Subject as SubjectModel
from school.forms import StudentForm
import json
# Create your views here.

class Student(View):
    def get(self,request):
        data = serializers.serialize('json' , StudentModel.objects.all())
        return JsonResponse(data, safe=False)

    def post(self , request):
        form = StudentForm(json.loads(request.body))
        if form.is_valid():   
            form.save()
            return JsonResponse({'message':'Student created successfully'}, status=201)
        else:
            return JsonResponse({'message':form.errors}, status=422)

class SpecficStudent(View):
    def get(self , request , *args , **kwargs):
        data = serializers.serialize('json' , StudentModel.objects.filter(id=kwargs['id']))
        return JsonResponse(data, safe=False)

    def post(self , request , *args , **kwargs):
        form = StudentForm(json.loads(request.body))
        if form.is_valid():   
            form.save()
            return JsonResponse({'message':'Student created successfully'}, status=201)
        else:
            return JsonResponse({'message':form.errors}, status=422)

    def put(self , request , *args , **kwargs):
        data = json.loads(request.body)
        form = StudentForm(data)
        if form.is_valid():
            student = StudentModel.objects.get(id=kwargs['id']).update(**data)
            return JsonResponse({'message':'Student updated successfully'}, status=201)
        return JsonResponse({'message':form.errors}, status=422)

    def delete(self , request , *args , **kwargs):
        StudentModel.objects.filter(id=kwargs['id']).delete()
        return JsonResponse({'message':'Student deleted successfully'}, status=201)

class Parent(View):
    def get(self , request):
        data = serializers.serialize('json' , ParentModel.objects.all())
        return JsonResponse(data, safe=False)

    def post(self , request):
        data = json.loads(request.body)
        ParentModel.objects.create(**data)
        return JsonResponse({'message':'Parent created successfully'}, status=201)

class SpecficParent(View):
    def get(self , request , *args , **kwargs):
        data = serializers.serialize('json' , ParentModel.objects.filter(id=kwargs['id']))
        return JsonResponse(data, safe=False)

    def post(self , request , *args , **kwargs):
        data = json.loads(request.body)
        ParentModel.objects.create(**data)
        return JsonResponse({'message':'Parent created successfully'}, status=201)

    def put(self , request , *args , **kwargs):
        data = json.loads(request.body)
        ParentModel.objects.filter(id=kwargs['id']).update(**data)
        return JsonResponse({'message':'Parent updated successfully'}, status=201)
        

    def delete(self , request , *args , **kwargs):
        ParentModel.objects.filter(id=kwargs['id']).delete()
        return JsonResponse({'message':'Parent deleted successfully'}, status=201)

class Subject(View):
    def get(self , request):
        data = serializers.serialize('json' , SubjectModel.objects.all())
        return JsonResponse(data, safe=False)
        
    def post(self , request):
        data = json.loads(request.body)
        SubjectModel.objects.create(**data)
        return JsonResponse({'message':'Subject created successfully'}, status=201)

class SpecficSubject(View):
    def get(self , request , *args , **kwargs):
        data = serializers.serialize('json' , SubjectModel.objects.filter(id=kwargs['id']))
        return JsonResponse(data, safe=False)

    def post(self , request , *args , **kwargs):
        data = json.loads(request.body)
        SubjectModel.objects.create(**data)
        return JsonResponse({'message':'Subject created successfully'}, status=201)
        

    def put(self , request , *args , **kwargs):
        data = json.loads(request.body)
        SubjectModel.objects.filter(id=kwargs['id']).update(**data)
        return JsonResponse({'message':'Subject updated successfully'}, status=201)
        
    def delete(self , request , *args , **kwargs):
        SubjectModel.objects.filter(id=kwargs['id']).delete()
        return JsonResponse({'message':'Subject deleted successfully'}, status=201)

