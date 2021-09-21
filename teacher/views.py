from django.shortcuts import render
from rest_framework import viewsets, status
from rest_framework.response import Response
from django.contrib.auth import authenticate
from django.contrib.auth.models import User

from .models import Teacher
from .serializers import TeacherSerializer

class TeacherViewSet(viewsets.ModelViewSet):
    queryset = Teacher.objects.all().order_by('-id')
    serializer_class = TeacherSerializer
    http_method_names = ['get', 'patch', 'put', 'delete']


class TeacherRegistrationViewSet(viewsets.ModelViewSet):
    queryset = Teacher.objects.all().order_by('-id')
    serializer_class = TeacherSerializer
    http_method_names = ['post']

    def create(self, request, *args, **kwargs):
        try:
            user = User.objects.create_user(request.data['email'], request.data['email'], request.data['password'])
            user.first_name = request.data['name']
            user.save()
        except Exception as e:
            print(e)
            user = None
        if user:
            request.data['user'] = user.pk
            serializer = self.get_serializer(data=request.data)
            if serializer.is_valid():
                try:
                    serializer.save()
                    return Response(serializer.data, status=status.HTTP_201_CREATED)
                except Exception as e:
                    return Response(e.__str__(), status=status.HTTP_400_BAD_REQUEST)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        return Response({'errors':{'user':'required'}}, status=status.HTTP_400_BAD_REQUEST)

class TeacherAuthenticationViewSet(viewsets.ModelViewSet):
    queryset = Teacher.objects.all().order_by('-id')
    serializer_class = TeacherSerializer
    http_method_names = ['post']

    def create(self, request, *args, **kwargs):
        username = request.data['email']
        password = request.data['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            serializer_teacher = TeacherSerializer(user.teacher)
            return Response(serializer_teacher.data, status=status.HTTP_200_OK)   
        return Response({'errors':{'email ou senha incorretos'}}, status=status.HTTP_401_UNAUTHORIZED)


    