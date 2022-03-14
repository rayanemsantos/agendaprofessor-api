from rest_framework import serializers
from .models import SchoolClass, ClassSubject, StudentSubject, ClassSubjectHistory
from student.serializers import StudentSerializer

class SchoolClassSerializer(serializers.ModelSerializer):

    class Meta:
        model = SchoolClass
        fields = '__all__'


class StudentSubjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudentSubject
        fields = '__all__'

    def to_representation(self, instance):
        response = super().to_representation(instance)
        response['student'] = '' if instance.student == "" or instance.student == None else StudentSerializer(instance.student).data
        return response

class ClassSubjectSerializer(serializers.ModelSerializer):
    students_subject = StudentSubjectSerializer(source="studentsubject_set", many=True, read_only=True)

    class Meta:
        model = ClassSubject
        fields = '__all__'

class ClassSubjectHistorySerializer(serializers.ModelSerializer):

    class Meta:
        model = ClassSubjectHistory
        fields = '__all__'




