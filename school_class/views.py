from re import sub
from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from django_filters.rest_framework import DjangoFilterBackend
from .models import SchoolClass, ClassSubject, StudentSubject, ClassSubjectHistory, StudentSubjectAverageGrade
from .serializers import SchoolClassSerializer, ClassSubjectSerializer, ClassSubjectHistorySerializer, StudentSubjectAverageGradeSerializer

from teacher.models import Teacher
from student.models import Student

class SchoolClassViewSet(viewsets.ModelViewSet):
    queryset = SchoolClass.objects.all().order_by('-id')
    serializer_class = SchoolClassSerializer
    http_method_names = ['get', 'post', 'patch', 'put', 'delete']
    filter_backends = (DjangoFilterBackend,)
    filter_fields = ('serie', 'identification', 'shift', 'ano')
    permission_classes = (IsAuthenticated,)

    @action(methods=['POST'], url_path='subject/add', url_name='subject/add', detail=True)
    def add_subject(self, request, pk):
        school_class = SchoolClass.objects.get(pk=pk)
        try:
            subject = request.data['subject']
            teacher = request.data['teacher']  

            teacher = Teacher.objects.get(pk=teacher)          

            subject = ClassSubject.objects.create(
                subject=subject,
                teacher=teacher,
                school_class=school_class
            )
            serializer_subject = ClassSubjectSerializer(subject)
            return Response(serializer_subject.data, status=status.HTTP_200_OK)   
        except Exception as e:
            return Response({'errors': str(e)}, status=status.HTTP_400_BAD_REQUEST)           

    @action(methods=['POST'], url_path='students/add', url_name='students/add', detail=True)
    def add_student(self, request, pk):
        school_class = SchoolClass.objects.get(pk=pk)
        school_class_subjects = school_class.classsubject_set.all()
        try:
            student = request.data['student']  
            if isinstance(student, list):
                for _sub in school_class_subjects:
                    for _st in student:
                        subject, _ = StudentSubject.objects.get_or_create(
                            class_subject=_sub,
                            student_id=_st,
                        ) 
                return Response(status=status.HTTP_200_OK)   
        except Exception as e:
            print(e)
            return Response({'errors': str(e)}, status=status.HTTP_400_BAD_REQUEST)   
        return Response({'errors': 'student must be a list'}, status=status.HTTP_400_BAD_REQUEST)      


class ClassSubjectViewSet(viewsets.ModelViewSet):
    queryset = ClassSubject.objects.all().order_by('-id')
    serializer_class = ClassSubjectSerializer
    http_method_names = ['get', 'post', 'patch', 'put', 'delete']    
    permission_classes = (IsAuthenticated,)

    @action(methods=['POST'], url_path='student/add', url_name='student/add', detail=True)
    def add_student(self, request, pk):
        school_class_subject = ClassSubject.objects.get(pk=pk)
        try:
            student = request.data['student']  
            if isinstance(student, list):
                subjects = list()
                for item in student:
                    student = Student.objects.get(pk=item) 
                    subject, _ = StudentSubject.objects.get_or_create(
                        school_class_subject=school_class_subject,
                        student=student,
                    ) 
                    subjects.append(subject)           
                serializer_subject = ClassSubjectSerializer(subjects, many=True)   
            else:     
                student = Student.objects.get(pk=student)          
                subject, _ = StudentSubject.objects.get_or_create(
                    school_class_subject=school_class_subject,
                    student=student,
                )
                serializer_subject = ClassSubjectSerializer(subject)
            return Response(serializer_subject.data, status=status.HTTP_200_OK)   
        except Exception as e:
            print(e)
            return Response({'errors': str(e)}, status=status.HTTP_400_BAD_REQUEST)    

    @action(methods=['POST'], url_path='history/add', url_name='history/add', detail=True)
    def add_history(self, request, pk):
        class_subject = ClassSubject.objects.get(pk=pk)
        try:
            comment = request.data['comment']   
            content = request.data['content']   
            presence = request.data['presence']   
            subject_history, _ = ClassSubjectHistory.objects.get_or_create(
                class_subject=class_subject,
                content=content,
                comment=comment
            )
            if isinstance(presence, list):
                for _pr in presence:
                    subject_history.classsubjecthistorypresence_set.create(
                        student_id=_pr['student'],
                        presence=_pr['presence'],
                    )
            serializer_subject = ClassSubjectHistorySerializer(subject_history)
            return Response(serializer_subject.data, status=status.HTTP_200_OK)   
        except Exception as e:
            return Response({'errors': str(e)}, status=status.HTTP_400_BAD_REQUEST)      