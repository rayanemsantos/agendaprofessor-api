from rest_framework import serializers
from .models import Student


class StudentSerializer(serializers.ModelSerializer):
    school_class = serializers.SerializerMethodField()

    class Meta:
        model = Student
        fields = '__all__'

    def is_valid(self, raise_exception=False):
        self.registration_id = self.initial_data.pop('registration_id', None)
        return super(StudentSerializer, self).is_valid(raise_exception)

    def get_school_class(self, obj):
        try:
            return obj.studentsubject_set.first().class_subject.school_class.__str__()
        except:
            return 'Sem turma'

    def to_representation(self, instance):
        response = super().to_representation(instance)
        response['full_name'] = instance.full_name
        return response
