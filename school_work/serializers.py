from rest_framework import serializers
from .models import SchoolWork, SchoolWorkManage

class SchoolWorkSerializer(serializers.ModelSerializer):

    class Meta:
        model = SchoolWork
        fields = '__all__'

class SchoolWorkManageSerializer(serializers.ModelSerializer):

    class Meta:
        model = SchoolWorkManage
        fields = '__all__'


        