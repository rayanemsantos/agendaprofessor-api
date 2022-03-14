from django.urls import path
from rest_framework import routers

from .views import SchoolClassViewSet, ClassSubjectViewSet

app_name = "school_class"

routeList = (
    (r'school_class', SchoolClassViewSet),
    (r'school_class_subject', ClassSubjectViewSet),
)
