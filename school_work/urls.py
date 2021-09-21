from django.urls import path
from .views import SchoolWorkViewSet

app_name = "school_work"

routeList = (
    (r'school_work', SchoolWorkViewSet),
)
