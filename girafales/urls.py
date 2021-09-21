from django.contrib import admin
from django.urls import path, include
from rest_framework import routers

from teacher import urls as teacher_urls
from student import urls as student_urls
from school_class import urls as school_class_urls
from school_work import urls as school_work_urls
from general import urls as general_urls

router = routers.DefaultRouter()

routeLists = [
    teacher_urls.routeList,
    student_urls.routeList,
    student_urls.routeList,
    school_class_urls.routeList,
    school_work_urls.routeList,
    general_urls.routeList
]

for routeList in routeLists:
    for route in routeList:
        router.register(route[0], route[1])

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
]
