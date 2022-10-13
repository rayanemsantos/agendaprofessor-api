from django.urls import path
from .views import BaseAuthenticationViewSet

app_name = "auth"

urlpatterns = [
    path('login', BaseAuthenticationViewSet.as_view(
        {'post': 'authenticate'}), name="login"),
    path('logout', BaseAuthenticationViewSet.as_view(
        {'post': 'logout'}), name="logout"),
    path('change_password', BaseAuthenticationViewSet.as_view(
        {'post': 'change_password'}), name="change_password"),
]
