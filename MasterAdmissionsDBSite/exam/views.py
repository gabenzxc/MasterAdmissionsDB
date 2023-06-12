from django.shortcuts import get_object_or_404
from rest_framework import viewsets
from .models import Exam
from .serializers import ExamSerializer
from rest_framework.permissions import IsAuthenticated

class ExamViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    queryset = Exam.objects.all()
    serializer_class = ExamSerializer