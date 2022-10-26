from django.urls import path , include
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


    path('student/', include([
			path('', Student.as_view()),
			path('<int:id>/', SpecficStudent.as_view())
		])),
	path('parent/', include([
			path('', Parent.as_view()),
            path('<int:id>/', SpecficParent.as_view())
		])),
    path('subject/', include([
			path('', Subject.as_view()),
            path('<int:id>/', SpecficSubject.as_view())
		]))
]