from django.urls import path
from rest_framework import routers

from .views import StudentViewSet

app_name = "student"

routeList = (
    (r'student', StudentViewSet),
)
