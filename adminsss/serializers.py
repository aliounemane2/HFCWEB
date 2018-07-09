from rest_framework import serializers
from essaies.models import *
from adminsss.models import *



class AdminsssssSerializer(serializers.ModelSerializer):
    class Meta:
        model = adminss
        fields = '__all__'

