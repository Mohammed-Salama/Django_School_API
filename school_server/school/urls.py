from django.urls import path
from school.views import Student
from school.views import SpecficStudent
from school.views import Parent
from school.views import SpecficParent
from school.views import Subject
from school.views import SpecficSubject

urlpatterns=[
    path('student',Student.as_view()),
    path('student/<int:id>',SpecficStudent.as_view()),
    path('parent',Parent.as_view()),
    path('parent/<int:id>',SpecficParent.as_view()),
    path('subject',Subject.as_view()),
    path('subject/<int:id>',SpecficSubject.as_view()),
]