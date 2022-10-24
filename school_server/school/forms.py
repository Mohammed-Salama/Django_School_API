from django import forms
from school.models import Student
from django.forms import ValidationError


def check_mark(value):
	if value < 0:
		raise ValidationError('Mark must be greater than 0')

def check_age(value):
	if value < 6:
		raise ValidationError('Age must be greater than 6')
class StudentForm(forms.ModelForm):
    mark = forms.IntegerField(required=False, validators=[check_mark])
    age = forms.IntegerField(required=False, validators=[check_age])
    class Meta:
        model = Student
        fields = "__all__"
        