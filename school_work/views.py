from django.http import Http404

from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.decorators import action
from .models import SchoolWork, SchoolWorkDeliveryManage
from .serializers import SchoolWorkSerializer, SchoolWorkDeliveryManageSerializer

from student.models import Student

class SchoolWorkViewSet(viewsets.ModelViewSet):
    queryset = SchoolWork.objects.all().order_by('-id')
    serializer_class = SchoolWorkSerializer
    http_method_names = ['get', 'post', 'patch', 'put', 'delete']

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

    @action(methods=['POST'], url_path='register_delivery', url_name='register_delivery', detail=True)
    def register_delivery(self, request, pk):
        school_work = SchoolWork.objects.get(pk=pk)
        try:
            student = request.data['student']  
            if isinstance(student, list):
                subjects = list()
                for item in student:
                    student = Student.objects.get(pk=item) 
                    subject, _ = SchoolWorkDeliveryManage.objects.get_or_create(
                        school_work=school_work,
                        student=student,
                        delivered=True,
                    ) 
                    subjects.append(subject)           
                serializer_subject = SchoolWorkDeliveryManageSerializer(subjects, many=True)   
            else:     
                student = Student.objects.get(pk=student)          
                subject, _ = SchoolWorkDeliveryManage.objects.get_or_create(
                    school_work=school_work,
                    student=student,
                    delivered=True,
                )
                serializer_subject = SchoolWorkDeliveryManageSerializer(subject)
            return Response(serializer_subject.data, status=status.HTTP_200_OK)   
        except Exception as e:
            print(e)
            return Response({'errors': str(e)}, status=status.HTTP_400_BAD_REQUEST)    