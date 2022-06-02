from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from .models import Student
from .serializers import StudentSerializer

class StudentViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all().order_by('-id')
    serializer_class = StudentSerializer
    http_method_names = ['get', 'post', 'patch', 'put', 'delete']
    permission_classes = (IsAuthenticated,)
    