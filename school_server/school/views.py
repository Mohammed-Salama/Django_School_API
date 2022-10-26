from rest_framework.views import APIView
from rest_framework.response import Response
from school.models import Student as StudentModel , Parent as ParentModel , Subject as SubjectModel
from school.serializers import StudentSerializer , ParentSerializer , SubjectSerializer
from rest_framework import mixins , generics , status
import json
# Create your views here.

class Student(APIView):
    def get(self,request):
        data = StudentSerializer(StudentModel.objects.all(), many=True)
        return Response(data.data)

    def post(self , request):
        serializer = StudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

class SpecficStudent(APIView):
    def get(self , request , id):
        try:
            data = StudentSerializer(StudentModel.objects.get(id=id))
            return Response(data.data)
        except StudentModel.DoesNotExist:
            return Response(status.HTTP_404_NOT_FOUND)

    def put(self , request , id):
        try:
            serializer = StudentSerializer(instance=StudentModel.objects.get(id=id) , data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors)
        except StudentModel.DoesNotExist:
            return Response(status.HTTP_404_NOT_FOUND)

    def delete(self , request , id):
        try:
            StudentModel.objects.get(id=id).delete()
            return Response(status.HTTP_200_OK)
        except StudentModel.DoesNotExist:
            return Response(status.HTTP_404_NOT_FOUND)
        
class Parent(generics.GenericAPIView, mixins.ListModelMixin, mixins.CreateModelMixin):
    queryset= ParentModel.objects.all()
    serializer_class = ParentSerializer
    def get (self, request , *args, **kwargs):
        return self.list(request , *args, **kwargs)

    def post(self, request , *args, **kwargs):
        return self.create(request , *args, **kwargs)

class SpecficParent(generics.GenericAPIView, mixins.RetrieveModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin):
    queryset= ParentModel.objects.all()
    serializer_class = ParentSerializer
    def get (self, request , *args, **kwargs):
        return self.retrieve(request , *args, **kwargs)

    def put(self, request , *args, **kwargs):
        return self.update(request , *args, **kwargs)

    def delete(self, request , *args, **kwargs):
        return self.destroy(request , *args, **kwargs)
    

class Subject(generics.ListAPIView , generics.CreateAPIView):
    queryset= SubjectModel.objects.all()
    serializer_class = SubjectSerializer


class SpecficSubject( generics.RetrieveAPIView , generics.UpdateAPIView , generics.DestroyAPIView):
    queryset= SubjectModel.objects.all()
    serializer_class = SubjectSerializer

