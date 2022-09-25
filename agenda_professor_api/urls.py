from django.contrib import admin
from django.urls import path, include
from rest_framework import routers

from teacher import urls as teacher_urls
from student import urls as student_urls
from school_class import urls as school_class_urls
from school_work import urls as school_work_urls
from general import urls as general_urls
from school_staff import urls as school_staff_urls
from base_auth import urls as base_auth_urls

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

from drf_yasg.views import get_schema_view
from drf_yasg import openapi

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



schema_view = get_schema_view(
    openapi.Info(
        title='Agenda do professor API',
        default_version='1.0.0'
    ),
    public=True,
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/general/',  include(general_urls.general_urlpatterns)),
    path('api/auth/',  include(base_auth_urls.urlpatterns)),
    path('api/doc/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
]