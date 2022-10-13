from urllib import response
from rest_framework import viewsets, status
from rest_framework.response import Response
from django.contrib.auth import authenticate, logout
from drf_yasg.utils import swagger_auto_schema
from rest_framework_simplejwt.tokens import RefreshToken
from .serializers import BaseUserSerializer, SwaggerPasswordChange, UserSerializer
from teacher.serializers import TeacherSerializer
from student.serializers import StudentSerializer
from school_staff.serializers import SchoolStaffSerializer


class BaseAuthenticationViewSet(viewsets.GenericViewSet):
    serializer_class = BaseUserSerializer
    http_method_names = ['post']

    def authenticate(self, request, *args, **kwargs):
        username = request.data['username']
        password = request.data['password']
        user = authenticate(request, username=username, password=password)

        if user:
            try:
                user_data_serializer = TeacherSerializer(user.teacher)
            except:
                pass

            try:
                user_data_serializer = StudentSerializer(user.student)
            except:
                pass

            try:
                user_data_serializer = SchoolStaffSerializer(user.schoolstaff)
            except:
                pass

            refresh = RefreshToken.for_user(user)
            serializer = UserSerializer(user)

            merged = dict()
            merged.update(user_data_serializer.data)
            merged.update(serializer.data)

            data = {
                'refresh': str(refresh),
                'access': str(refresh.access_token),
                'data': merged
            }
            return Response(data, status=status.HTTP_200_OK)
        return Response({'errors': {'email ou senha incorretos'}}, status=status.HTTP_401_UNAUTHORIZED)

    def logout(self, request, *args, **kwargs):
        try:
            logout(request)
            return Response(status=status.HTTP_200_OK)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)

    @swagger_auto_schema(request_body=SwaggerPasswordChange, responses={200: ''})
    def change_password(self, request, *args, **kwargs):
        try:
            password = request.data['password']
            current_passord = request.data['current_passord']
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)

        validate_current_password = request.user.check_password(
            current_passord)

        if validate_current_password:
            request.user.set_password(password)
            request.user.save()
            return Response(status=status.HTTP_200_OK)
        return Response({'error': 'Senha atual inválida'}, status=status.HTTP_400_BAD_REQUEST)
