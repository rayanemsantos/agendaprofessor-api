from re import sub
from datetime import datetime
from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from django_filters.rest_framework import DjangoFilterBackend
from .models import SchoolClass, ClassSubject, StudentSubject, ClassSubjectHistory, StudentSubjectAverageGrade
from .serializers import SchoolClassSerializer, ClassSubjectSerializer, ClassSubjectHistorySerializer, StudentSubjectAverageGradeSerializer
from rest_framework_simplejwt.authentication import JWTAuthentication
from teacher.models import Teacher
from student.models import Student
from rest_framework.authentication import BasicAuthentication, get_authorization_header


class SchoolClassViewSet(viewsets.ModelViewSet):
    queryset = SchoolClass.objects.all().order_by('-id')
    serializer_class = SchoolClassSerializer
    http_method_names = ['get', 'post', 'patch', 'put', 'delete']
    filter_backends = (DjangoFilterBackend,)
    filter_fields = ('serie', 'identification', 'shift', 'ano')
    permission_classes = (IsAuthenticated,)

    def list(self, request, *args, **kwargs):
        queryset = SchoolClass.objects.all()

        if request.user.teacher:
            queryset = queryset.filter(
                classsubject__teacher__in=[request.user.teacher.id])

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

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
    authentication_classes = (JWTAuthentication,)

    def list(self, request, *args, **kwargs):
        queryset = ClassSubject.objects.all()
        if request.user.teacher:
            queryset = queryset.filter(teacher=request.user.teacher)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

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
                serializer_subject = ClassSubjectSerializer(
                    subjects, many=True)
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
            list_presence = request.data['list_presence']
            subject_history, _ = ClassSubjectHistory.objects.get_or_create(
                class_subject=class_subject,
                content=content,
                comment=comment
            )
            if isinstance(list_presence, list):
                for _pr in list_presence:
                    subject_history.classsubjecthistorypresence_set.create(
                        student_id=_pr['student'],
                        presence=_pr['presence'],
                    )
            serializer_subject = ClassSubjectHistorySerializer(subject_history)
            return Response(serializer_subject.data, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({'errors': str(e)}, status=status.HTTP_400_BAD_REQUEST)

    @action(methods=['PUT'], url_path='history/update', url_name='history/update', detail=True)
    def update_history(self, request, pk):
        class_subject = ClassSubject.objects.get(pk=pk)
        try:
            comment = request.data['comment']
            content = request.data['content']
            list_presence = request.data['list_presence']

            subject_history, _ = class_subject.classsubjecthistory_set.first().update(
                content=content,
                comment=comment
            )
            if isinstance(list_presence, list):
                for _pr in list_presence:
                    subject_history.classsubjecthistorypresence_set.update(
                        student_id=_pr['student'],
                        presence=_pr['presence'],
                    )
            serializer_subject = ClassSubjectHistorySerializer(subject_history)
            return Response(serializer_subject.data, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({'errors': str(e)}, status=status.HTTP_400_BAD_REQUEST)


class ClassSubjectHistoryViewSet(viewsets.ModelViewSet):
    queryset = ClassSubjectHistory.objects.all().order_by('-id')
    serializer_class = ClassSubjectHistorySerializer
    http_method_names = ['get', 'post', 'patch', 'put', 'delete']
    filter_backends = (DjangoFilterBackend,)
    filter_fields = ('class_subject', )
    permission_classes = [IsAuthenticated, ]
    authentication_classes = (JWTAuthentication,)

    def create(self, request, *args, **kwargs):
        class_subject = request.data['class_subject']
        print('class_subject', class_subject)
        today = datetime.today()
        already_registered_for_the_day = ClassSubjectHistory.objects.filter(
            class_subject=class_subject).exists()
        if already_registered_for_the_day:
            return Response({'message': 'Aula do dia já foi registrada'}, status=status.HTTP_400_BAD_REQUEST)

        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
