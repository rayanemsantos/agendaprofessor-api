from rest_framework import serializers
from .models import SchoolStaff
from base_auth.serializers import UserSerializer

class SchoolStaffSerializer(serializers.ModelSerializer):

    class Meta:
        model = SchoolStaff
        fields = '__all__'

    def to_representation(self, instance):
        response = super().to_representation(instance)
        response['user'] = '' if instance.user == "" or instance.user == None else UserSerializer(instance.user).data
        return response