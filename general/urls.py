from django.urls import path

from .views import CalendarEventViewSet, DashboardCountViewSet

app_name = "calendar_event"

routeList = (
    (r'calendar_event', CalendarEventViewSet),
)

general_urlpatterns = [
    path('dashboard_infos', DashboardCountViewSet.as_view(), name="dashboard_infos"),
]