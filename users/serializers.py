from rest_framework import serializers
from users.models import *



class Utilisateur2Serializer(serializers.ModelSerializer):
    class Meta:
        model = utilisateur2
        fields = '__all__'



class Type_AbonnementSerializer(serializers.ModelSerializer):
    class Meta:
        model = Type_Abonnement
        fields = '__all__'




class PaiementSerializer(serializers.ModelSerializer):
    class Meta:
        model = Paiement
        fields = '__all__'