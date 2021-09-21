from django.urls import path
from rest_framework import routers

from .views import SchoolClassViewSet, SchoolClassSubjectViewSet

app_name = "school_class"

routeList = (
    (r'school_class', SchoolClassViewSet),
    (r'school_class_subject', SchoolClassSubjectViewSet),
)
