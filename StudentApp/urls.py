from django.urls import path
from StudentApp import views

urlpatterns = [
    path('', views.register_student, name='register_student'),
    path('students/', views.student_list, name='student_list'),
    path('courses/', views.course_list, name='course_list'),
    path('courses/<int:course_id>/', views.course_detail, name='course_detail'),
]
