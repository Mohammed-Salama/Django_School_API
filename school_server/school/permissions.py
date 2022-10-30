from rest_framework import authentication
from rest_framework import exceptions
from school.models import Token , User
from rest_framework import permissions
class Authenticate(authentication.BaseAuthentication):
	def authenticate(self, request):
         header_token = request.headers.get('Authorization')
         token = Token.objects.filter(token=header_token)
         if token:
            return(True,None)
         raise exceptions.AuthenticationFailed('Invalid Token')

class StudentListPermission(permissions.BasePermission):

	def has_permission(self, request, view):
         user_id = Token.objects.get(token=request.headers.get('Authorization')).user_id
         user = User.objects.get(id=user_id)
         if user.type == 'parent':
            return True
         return False

class SpecificStudentPermission(permissions.BasePermission):

    def has_permission(self, request, view):
         user_id = Token.objects.get(token=request.headers.get('Authorization')).user_id
         user = User.objects.get(id=user_id)
         children = User.objects.filter(parent=user_id)
         if children.filter(id=view.kwargs['id']):
            return True
         self.message = 'invalid student'
         return False