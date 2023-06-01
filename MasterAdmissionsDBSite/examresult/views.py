from django.shortcuts import get_object_or_404
from rest_framework import viewsets
from .models import  ExamResult
from .serializers import ExamResultSerializer

class ExamResultViewSet(viewsets.ModelViewSet):
    queryset = ExamResult.objects.all()
    serializer_class = ExamResultSerializer