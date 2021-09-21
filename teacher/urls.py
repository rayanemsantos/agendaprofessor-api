from django.urls import path
from rest_framework import routers

from .views import TeacherViewSet, TeacherRegistrationViewSet, TeacherAuthenticationViewSet

app_name = "teacher"

routeList = (
    (r'teacher', TeacherViewSet),
    (r'user/teacher/registration', TeacherRegistrationViewSet),
    (r'user/teacher/authentication', TeacherAuthenticationViewSet),
)
