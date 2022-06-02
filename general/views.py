from django.http import Http404
from rest_framework.response import Response
from rest_framework import viewsets, status
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated

from school_class.models import SchoolClass
from student.models import Student
from teacher.models import Teacher
from .models import CalendarEvent
from .serializers import CalendarEventSerializer

class CalendarEventViewSet(viewsets.ModelViewSet):
    queryset = CalendarEvent.objects.all().order_by('-id')
    serializer_class = CalendarEventSerializer
    http_method_names = ['get', 'post', 'patch', 'put', 'delete']
    permission_classes = (IsAuthenticated,)
    
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, *args, **kwargs):
        try:
            instance = self.get_object()
            self.perform_destroy(instance)
        except Http404:
            pass
        return Response(status=status.HTTP_204_NO_CONTENT)  

class DashboardCountViewSet(APIView):
    http_method_names = ['get']
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        students = Student.objects.all().count()
        teachers = Teacher.objects.all().count()
        schoolclass = SchoolClass.objects.all().count()
        calendarevents = CalendarEvent.objects.all().count()

        items = [
            {
                'field': 'Estudantes',
                'count': students,
                'path': 'alunos'
            },
            {
                'field': 'Professores',
                'count': teachers,
                'path': 'professores'
            },
            {
                'field': 'Turmas',
                'count': schoolclass,
                'path': 'turmas'
            },
            {
                'field': 'Eventos',
                'count': calendarevents,
                'path': ''
            },

        ]
        return Response({'data': items}, status=status.HTTP_200_OK)
