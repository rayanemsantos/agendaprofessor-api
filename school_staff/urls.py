from .views import SchoolStaffAuthenticationViewSet

app_name = "staff"

routeList = (
    (r'user/staff/authentication', SchoolStaffAuthenticationViewSet),
)
