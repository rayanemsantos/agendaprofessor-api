from django.contrib import admin
from django.urls import path, include
from rest_framework import routers

from teacher import urls as teacher_urls
from student import urls as student_urls
from school_class import urls as school_class_urls
from school_work import urls as school_work_urls
from general import urls as general_urls
from school_staff import urls as school_staff_urls

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

router = routers.DefaultRouter()

routeLists = [
    teacher_urls.routeList,
    student_urls.routeList,
    student_urls.routeList,
    school_class_urls.routeList,
    school_work_urls.routeList,
    general_urls.routeList,
    school_staff_urls.routeList
]

for routeList in routeLists:
    for route in routeList:
        router.register(route[0], route[1])

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/general/',  include(general_urls.general_urlpatterns)),
]
