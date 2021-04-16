from .models import Threat
from rest_framework import serializers

class ThreatSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Threat
        fields = ['email', 'severity', 'isRemediated']