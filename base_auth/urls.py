from django.urls import path
from .views import BaseAuthenticationViewSet

app_name = "auth"

urlpatterns = [
    path('login', BaseAuthenticationViewSet.as_view({'post': 'authenticate'}), name="login"),
    path('logout', BaseAuthenticationViewSet.as_view({'post': 'logout'}), name="logout"),
]