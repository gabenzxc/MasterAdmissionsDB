from django.shortcuts import get_object_or_404
from rest_framework import viewsets
from .models import Application
from .serializers import  ApplicationSerializer
from rest_framework.permissions import IsAuthenticated

class ApplicationViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    queryset = Application.objects.all()
    serializer_class = ApplicationSerializer
