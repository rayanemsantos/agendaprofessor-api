from django.urls import path
from rest_framework import routers

from .views import SchoolClassViewSet, ClassSubjectViewSet, ClassSubjectHistoryViewSet, ClassSubjectHistoryPresenceViewSet, StudentSubjectAverageGradeViewSet

app_name = "school_class"

routeList = (
    (r'school_class', SchoolClassViewSet),
    (r'school_class_subject', ClassSubjectViewSet),
    (r'class_subject_history', ClassSubjectHistoryViewSet),
    (r'class_subject_history_presence', ClassSubjectHistoryPresenceViewSet),
    (r'student_subject_average_grade', StudentSubjectAverageGradeViewSet),
)

