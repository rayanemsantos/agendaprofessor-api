from re import sub
from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response

from .models import SchoolClass, SchoolClassSubject, SchoolClassStudent, SchoolClassSubjectHistory
from .serializers import SchoolClassSerializer, SchoolClassSubjectSerializer, SchoolClassSubjectHistorySerializer

from teacher.models import Teacher
from student.models import Student
from school_work.models import SchoolWork

class SchoolClassViewSet(viewsets.ModelViewSet):
    queryset = SchoolClass.objects.all().order_by('-id')
    serializer_class = SchoolClassSerializer
    http_method_names = ['get', 'post', 'patch', 'put', 'delete']

    @action(methods=['POST'], url_path='subject/add', url_name='subject/add', detail=True)
    def add_subject(self, request, pk):
        school_class = SchoolClass.objects.get(pk=pk)
        try:
            subject = request.data['subject']
            teacher = request.data['teacher']  

            teacher = Teacher.objects.get(pk=teacher)          

            subject = SchoolClassSubject.objects.create(
                subject=subject,
                teacher=teacher,
                school_class=school_class
            )
            serializer_subject = SchoolClassSubjectSerializer(subject)
            return Response(serializer_subject.data, status=status.HTTP_200_OK)   
        except Exception as e:
            return Response({'errors': str(e)}, status=status.HTTP_400_BAD_REQUEST)           


class SchoolClassSubjectViewSet(viewsets.ModelViewSet):
    queryset = SchoolClassSubject.objects.all().order_by('-id')
    serializer_class = SchoolClassSubjectSerializer
    http_method_names = ['get', 'post', 'patch', 'put', 'delete']    


    @action(methods=['POST'], url_path='student/add', url_name='student/add', detail=True)
    def add_student(self, request, pk):
        school_class_subject = SchoolClassSubject.objects.get(pk=pk)
        try:
            student = request.data['student']  
            if isinstance(student, list):
                subjects = list()
                for item in student:
                    student = Student.objects.get(pk=item) 
                    subject, _ = SchoolClassStudent.objects.get_or_create(
                        school_class_subject=school_class_subject,
                        student=student,
                    ) 
                    subjects.append(subject)           
                serializer_subject = SchoolClassSubjectSerializer(subjects, many=True)   
            else:     
                student = Student.objects.get(pk=student)          
                subject, _ = SchoolClassStudent.objects.get_or_create(
                    school_class_subject=school_class_subject,
                    student=student,
                )
                serializer_subject = SchoolClassSubjectSerializer(subject)
            return Response(serializer_subject.data, status=status.HTTP_200_OK)   
        except Exception as e:
            print(e)
            return Response({'errors': str(e)}, status=status.HTTP_400_BAD_REQUEST)    

    @action(methods=['POST'], url_path='history/add', url_name='history/add', detail=True)
    def add_history(self, request, pk):
        school_class_subject = SchoolClassSubject.objects.get(pk=pk)
        try:
            comment = request.data['comment']   
            content = request.data['content']   
            homework = request.data['homework']   
            classwork = request.data['classwork']   

            homework = SchoolWork.objects.get(pk=homework)
            classwork = SchoolWork.objects.get(pk=classwork)
            subject, _ = SchoolClassSubjectHistory.objects.get_or_create(
                school_class_subject=school_class_subject,
                content=content,
                comment=comment,
                homework=homework,
                classwork=classwork
            )
            serializer_subject = SchoolClassSubjectHistorySerializer(subject)
            return Response(serializer_subject.data, status=status.HTTP_200_OK)   
        except Exception as e:
            return Response({'errors': str(e)}, status=status.HTTP_400_BAD_REQUEST)                
