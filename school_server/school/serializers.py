from rest_framework import serializers
from django.forms import ValidationError
from school.models import Student , Parent , Subject


def check_mark(value):
	if value < 0:
		raise ValidationError('Mark must be greater than 0')

def check_age(value):
	if value < 6:
		raise ValidationError('Age must be greater than 6')

class StudentSerializer(serializers.ModelSerializer):
    mark = serializers.IntegerField(required=False, validators=[check_mark])
    age = serializers.IntegerField(required=False, validators=[check_age])
    class Meta:
        model = Student
        fields = "__all__"

class ParentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Parent
        fields = "__all__"

class SubjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subject
        fields = "__all__"
        