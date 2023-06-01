from django.shortcuts import get_object_or_404
from rest_framework import viewsets
from .models import Application
from .serializers import  ApplicationSerializer

# Create your views here.
class ApplicationViewSet(viewsets.ModelViewSet):
    queryset = Application.objects.all()
    serializer_class = ApplicationSerializer
