from rest_framework import serializers
from django.forms import ValidationError
from school.models import User , Subject , Token


def check_mark(value):
	if value < 0:
		raise ValidationError('Mark must be greater than 0')

def check_age(value):
	if value < 6:
		raise ValidationError('Age must be greater than 6')


class SubjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subject
        fields = "__all__"

class ParnetSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        exclude = ['password','type','mark','school_class','parent']
class UserSerializer(serializers.ModelSerializer):
    mark = serializers.IntegerField(required=False, validators=[check_mark])
    age = serializers.IntegerField(required=False, validators=[check_age])
    subjects = SubjectSerializer(many=True , required=False)
    username = serializers.CharField(required=True)
    password = serializers.CharField(required=True)
    parent = ParnetSerializer(required=False)
    school_class = serializers.IntegerField(required=False)
    class Meta:
        model = User
        fields = "__all__"

class AddUserSerializer(serializers.ModelSerializer):
    mark = serializers.IntegerField(required=False, validators=[check_mark])
    age = serializers.IntegerField(required=False, validators=[check_age])
    subjects = serializers.PrimaryKeyRelatedField(many=True , queryset=Subject.objects.all(), required=False)
    username = serializers.CharField(required=True)
    password = serializers.CharField(required=True)
    parent = serializers.PrimaryKeyRelatedField(queryset=User.objects.all(), required=False)
    school_class = serializers.IntegerField(required=False)
    class Meta:
        model = User
        fields = "__all__"

class TokenSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    class Meta:
        model = Token
        fields = "__all__"