from django.urls import path , include
from school.views import AddUser , Subject , SpecficSubject , LoginUser , StudentList , SpecficStudent

urlpatterns=[
    path('student/', include([
			path('', AddUser.as_view()),
			#path('<int:id>/', SpecficStudent.as_view())
		])),
	path('parent/', include([
			path('', AddUser.as_view()),
            path('students', StudentList.as_view()),
            path('<int:id>/', SpecficStudent.as_view())
		])),
    path('subject/', include([
			path('', Subject.as_view()),
            path('<int:id>/', SpecficSubject.as_view())
		])),
    path('login/', LoginUser.as_view()),
]