from django.shortcuts import get_object_or_404
from rest_framework import viewsets
from .models import  ExamResult
from .serializers import ExamResultSerializer
from rest_framework.permissions import IsAuthenticated

class ExamResultViewSet(viewsets.ModelViewSet):
    queryset = ExamResult.objects.all()
    permission_classes = (IsAuthenticated,)
    serializer_class = ExamResultSerializer