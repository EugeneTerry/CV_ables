from rest_framework import serializers
from CV_ables_api.models import Vita
from CV_ables_api.serializers import (
    ApplicantSerializer,
    MissionSerializer,
    ProspectSmSerializer
    )
class VitaSerializer(serializers.ModelSerializer):
    applicant = ApplicantSerializer(many=False)
    
    mission = MissionSerializer(many=False)
    
    prospect = ProspectSmSerializer(many=False)
    class Meta:
        model = Vita
        fields = (
            'id',
            'applicant',
            'mission',
            'prospect',
            'published',
            'slug'
        )