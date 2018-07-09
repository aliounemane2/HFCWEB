from rest_framework import serializers
from essaies.models import *



class Personne_essaieSerializer(serializers.ModelSerializer):
    class Meta:
        model = personne_essaie
        fields = '__all__'

