from django.urls import path
from . import views

urlpatterns = [
    path('',views.index, name='index'),
    path('index.html', views.index, name='index'),
    path('teacher', views.teacher, name='teacher'),
    path('register', views.register, name='register'),
    path('login', views.login, name='login'),
    path('student_dash', views.student_dash, name="student_dash"),
    path('teacher_dash', views.teacher_dash, name="teacher_dash"),
    path('grievance', views.grievance, name="new_grievance")
]