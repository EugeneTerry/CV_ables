from rest_framework import serializers
from CV_ables_api.models import Vita
from CV_ables_api.serializers import (
    ApplicantSerializer,
    JobtypeSerializer,
    MissionSmSerializer,
    ProspectSmSerializer
    )
class VitaSerializer(serializers.ModelSerializer):
    applicant = ApplicantSerializer(many=False)
    
    job_type = JobtypeSerializer(many=False)
    
    mission = MissionSmSerializer(many=False)
    
    prospect = ProspectSmSerializer(many=False)
    class Meta:
        model = Vita
        fields = (
            'id',
            'applicant',
            'job_type',
            'mission',
            'prospect',
            'published',
            'slug'
        )