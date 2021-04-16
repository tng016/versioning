from django.shortcuts import render

# Create your views here.

from .models import Threat
from rest_framework import viewsets
from rest_framework import permissions
from .serializer import ThreatSerializer

class ThreatsViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Threat.objects.all()
    serializer_class = ThreatSerializer
    permission_classes = [permissions.IsAuthenticated]