from rest_framework import serializers
from employers.models import *





class EmployersSerializer(serializers.ModelSerializer):
    class Meta:
        model = employers
        fields = '__all__'



class PointageSerializer(serializers.ModelSerializer):
    class Meta:
        model = pointage
        fields = '__all__'