from rest_framework import viewsets, status
from rest_framework.response import Response
from django.contrib.auth import authenticate
from .models import SchoolStaff
from .serializers import SchoolStaffSerializer
from rest_framework_simplejwt.tokens import RefreshToken

class SchoolStaffAuthenticationViewSet(viewsets.ModelViewSet):
    queryset = SchoolStaff.objects.all().order_by('-id')
    serializer_class = SchoolStaffSerializer
    http_method_names = ['post']

    def create(self, request, *args, **kwargs):
        username = request.data['email']
        password = request.data['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            refresh = RefreshToken.for_user(user)
            serializer_teacher = SchoolStaffSerializer(user.schoolstaff)

            data = {
                'refresh': str(refresh),
                'access': str(refresh.access_token),
                'data': serializer_teacher.data
            }    
            return Response(data, status=status.HTTP_200_OK)   
        return Response({'errors':{'email ou senha incorretos'}}, status=status.HTTP_401_UNAUTHORIZED)