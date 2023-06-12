from django.shortcuts import render
from rest_framework import viewsets
from .models import Abiturient
from .serializers import AbiturientSerializer
from rest_framework.permissions import IsAuthenticated

class AbiturientViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    
    queryset = Abiturient.objects.all()
    serializer_class = AbiturientSerializer