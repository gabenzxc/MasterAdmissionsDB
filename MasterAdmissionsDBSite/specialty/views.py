from django.shortcuts import get_object_or_404
from rest_framework import viewsets
from .models import Specialty
from .serializers import SpecialtySerializer

class SpecialtyViewSet(viewsets.ModelViewSet):
    queryset = Specialty.objects.all()
    serializer_class = SpecialtySerializer