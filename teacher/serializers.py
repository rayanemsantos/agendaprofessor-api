from rest_framework import serializers
from base_auth.serializers import UserSerializer
from .models import Teacher


class TeacherSerializer(serializers.ModelSerializer):

    class Meta:
        model = Teacher
        fields = '__all__'

    def to_representation(self, instance):
        response = super().to_representation(instance)
        response['user'] = '' if instance.user == "" or instance.user == None else UserSerializer(instance.user).data
        return response