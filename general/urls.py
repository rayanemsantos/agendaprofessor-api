from django.urls import path
from rest_framework import routers

from .views import CalendarEventViewSet

app_name = "calendar_event"

routeList = (
    (r'calendar_event', CalendarEventViewSet),
)
