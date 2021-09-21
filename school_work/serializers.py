from rest_framework import serializers
from .models import SchoolWork, SchoolWorkDeliveryManage

class SchoolWorkSerializer(serializers.ModelSerializer):

    class Meta:
        model = SchoolWork
        fields = '__all__'

class SchoolWorkDeliveryManageSerializer(serializers.ModelSerializer):

    class Meta:
        model = SchoolWorkDeliveryManage
        fields = '__all__'


        