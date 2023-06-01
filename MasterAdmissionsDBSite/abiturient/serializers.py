from rest_framework import serializers
from .models import Abiturient

class AbiturientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Abiturient
        fields = '__all__'