from django.shortcuts import render
from rest_framework import viewsets
from .models import Abiturient
from .serializers import AbiturientSerializer

# Create your views here.
class AbiturientViewSet(viewsets.ModelViewSet):
    queryset = Abiturient.objects.all()
    serializer_class = AbiturientSerializer