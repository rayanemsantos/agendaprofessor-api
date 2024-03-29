from rest_framework import serializers
from django.contrib.auth.models import User
from .models import BaseUser


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        exclude = ('id', 'password', )


class BaseUserSerializer(serializers.Serializer):

    class Meta:
        model = BaseUser
        fields = '__all__'


class SwaggerPasswordChange(serializers.Serializer):
    password = serializers.CharField()
    current_passord = serializers.CharField()

    class Meta:
        model = BaseUser
        fields = '__all__'
