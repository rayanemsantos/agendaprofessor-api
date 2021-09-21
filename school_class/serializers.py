from rest_framework import serializers
from .models import SchoolClass, SchoolClassSubject, SchoolClassStudent, SchoolClassSubjectHistory
from student.serializers import StudentSerializer

class SchoolClassSerializer(serializers.ModelSerializer):

    class Meta:
        model = SchoolClass
        fields = '__all__'


class SchoolClassStudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = SchoolClassStudent
        fields = '__all__'

    def to_representation(self, instance):
        response = super().to_representation(instance)
        response['student'] = '' if instance.student == "" or instance.student == None else StudentSerializer(instance.student).data
        return response

class SchoolClassSubjectSerializer(serializers.ModelSerializer):
    school_class_students = SchoolClassStudentSerializer(source="schoolclassstudent_set", many=True, read_only=True)

    class Meta:
        model = SchoolClassSubject
        fields = '__all__'

class SchoolClassSubjectHistorySerializer(serializers.ModelSerializer):

    class Meta:
        model = SchoolClassSubjectHistory
        fields = '__all__'




