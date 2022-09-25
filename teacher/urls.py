from .views import TeacherViewSet, TeacherRegistrationViewSet

app_name = "teacher"

routeList = (
    (r'teacher', TeacherViewSet),
    (r'teacher/registration', TeacherRegistrationViewSet),
)
