from django.contrib.auth.models import User, Group
from rest_framework import serializers
from .models import Hive, Check, Apiaries


class Apiaries_Serializer(serializers.ModelSerializer): 
    # pour manipulation spécifique de données mettre Serailizers.Serializer et détails ci-dessous
#    a_id = serializers.IntegerField(read_only=True)
#    a_name = serializers.CharField(max_length=15)
#    a_idgateway = serializers.CharField(max_length=15)
    class Meta:
        model = Apiaries
        fields = ['a_id', 'a_fkuser', 'a_name', 'a_idgateway']

    #def create(self, validated_data):
    #    return Apiaries.objects.create(**validated_data)


class Hives_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Hive
        fields = ['h_fkapiary', 'rfid_id', 'h_swarmdate', 'h_queendate', 
            'h_queentype', 'h_queencolor', 'h_model', 
            'h_framenb']


class Checks_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Check
        fields = '__all__'
