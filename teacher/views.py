from django.forms import ValidationError
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django.contrib.auth.password_validation import validate_password

from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated


from .models import Teacher
from .serializers import TeacherSerializer

class TeacherViewSet(viewsets.ModelViewSet):
    queryset = Teacher.objects.all().order_by('-id')
    serializer_class = TeacherSerializer
    http_method_names = ['get', 'patch', 'put', 'delete']
    permission_classes = (IsAuthenticated,)


class TeacherRegistrationViewSet(viewsets.ModelViewSet):
    queryset = Teacher.objects.all().order_by('-id')
    serializer_class = TeacherSerializer
    http_method_names = ['post']

    def create(self, request, *args, **kwargs):
        # name = request.data['full_name']
        # password = request.data['cpf'][:6] + name if not 'password' in request.data else request.data['password']

        # try:
        #     validate_password(password)
        # except ValidationError as error:
        #     return Response({'errors': str(error)}, status=status.HTTP_400_BAD_REQUEST)       
        # try:
        #     user = User.objects.create_user(request.data['email'], request.data['email'], password)
        #     user.save()
        #     request.data['user'] = user.pk
        # except Exception as e:
        #     print(e)
        #     return Response({'errors': str(e)}, status=status.HTTP_400_BAD_REQUEST)
        try:
            serializer = self.get_serializer(data=request.data)
            if serializer.is_valid():
                try:
                    serializer.save()
                    return Response(serializer.data, status=status.HTTP_201_CREATED)
                except Exception as e:
                    return Response(e.__str__(), status=status.HTTP_400_BAD_REQUEST)                   
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({'errors': str(e)}, status=status.HTTP_400_BAD_REQUEST)

class TeacherAuthenticationViewSet(viewsets.ModelViewSet):
    queryset = Teacher.objects.all().order_by('-id')
    serializer_class = TeacherSerializer
    http_method_names = ['post']

    def create(self, request, *args, **kwargs):
        username = request.data['email']
        password = request.data['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            refresh = RefreshToken.for_user(user)
            serializer_teacher = TeacherSerializer(user.teacher)
            
            data = {
                'refresh': str(refresh),
                'access': str(refresh.access_token),
                'data': serializer_teacher.data
            }              
            return Response(data, status=status.HTTP_200_OK)   
        return Response({'errors':{'email ou senha incorretos'}}, status=status.HTTP_401_UNAUTHORIZED)


    