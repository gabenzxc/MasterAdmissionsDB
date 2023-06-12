from django.shortcuts import get_object_or_404
from rest_framework import viewsets
from .models import Specialty
from .serializers import SpecialtySerializer
from rest_framework.permissions import IsAuthenticated

class SpecialtyViewSet(viewsets.ModelViewSet):
    queryset = Specialty.objects.all()
    permission_classes = (IsAuthenticated,)
    serializer_class = SpecialtySerializer