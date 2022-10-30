from rest_framework.views import APIView
from rest_framework.response import Response
from school.models import  Subject as SubjectModel , User as UserModel , Token as TokenModel
from school.serializers import UserSerializer , SubjectSerializer , AddUserSerializer , TokenSerializer
from school.encrypt import create_jwt
from rest_framework import mixins , generics , status
from school.permissions import Authenticate , StudentListPermission , SpecificStudentPermission

# Create your views here.

class AddUser(APIView):
    def post(self , request):
        # if (request.data['type'] == 'student'):
        #     parent_id = request.data['parent']
        #     parent = UserModel.objects.get(id=parent_id)
        #     request.data['parent'] = parent
        serializer = AddUserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

class LoginUser(APIView):
    def post(self , request):
        username = request.data.get('username')
        password = request.data.get('password')
        user = UserModel.objects.filter(username=username , password=password)
        if user:
            access_token = create_jwt(username , password)
            token = TokenModel.objects.create(token=access_token , user=user[0])
            return Response({'token':access_token})
        return Response({'error':'invalid username or password'})

class StudentList(generics.GenericAPIView , mixins.ListModelMixin):
    serializer_class = UserSerializer
    queryset = UserModel.objects.all()
    authentication_classes = [Authenticate]
    permission_classes = [StudentListPermission]
    def get(self , request):
        token = request.headers.get('Authorization')
        user_id = TokenModel.objects.get(token=token).id
        students = UserModel.objects.filter(parent=user_id)
        serializer = UserSerializer(students , many=True)
        return Response(serializer.data)
class SpecficStudent(generics.GenericAPIView , mixins.RetrieveModelMixin , mixins.UpdateModelMixin , mixins.DestroyModelMixin):
    serializer_class = UserSerializer
    queryset = UserModel.objects.all()
    authentication_classes = [Authenticate]
    permission_classes = [SpecificStudentPermission]
    def get(self , request , id):
            student = UserModel.objects.get(id=id)
            serializer = UserSerializer(student)
            return Response(serializer.data)

    def put(self , request , id):
        serializer = UserSerializer(instance=UserModel.objects.get(id=id) , data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)
    

    def delete(self , request , id):
        try:
            UserModel.objects.get(id=id).delete()
            return Response(status.HTTP_200_OK)
        except UserModel.DoesNotExist:
            return Response(status.HTTP_404_NOT_FOUND)
        
    

class Subject(generics.ListAPIView , generics.CreateAPIView):
    queryset= SubjectModel.objects.all()
    serializer_class = SubjectSerializer


class SpecficSubject( generics.RetrieveAPIView , generics.UpdateAPIView , generics.DestroyAPIView):
    queryset= SubjectModel.objects.all()
    serializer_class = SubjectSerializer

