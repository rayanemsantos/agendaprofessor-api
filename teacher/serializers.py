from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Teacher

class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'first_name']


class TeacherSerializer(serializers.ModelSerializer):

    class Meta:
        model = Teacher
        fields = '__all__'

    def to_representation(self, instance):
        response = super().to_representation(instance)
        response['user'] = '' if instance.user == "" or instance.user == None else UserSerializer(instance.user).data
        return response