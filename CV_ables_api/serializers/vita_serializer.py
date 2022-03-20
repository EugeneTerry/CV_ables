from rest_framework import serializers
from CV_ables_api.models import Vita, jobtype
from CV_ables_api.serializers import (
    ApplicantSerializer,
    MissionSerializer,
    ProspectSmSerializer,
    JobtypeSerializer
    )
class VitaSerializer(serializers.ModelSerializer):
    applicant = ApplicantSerializer(many=False)
    
    mission = MissionSerializer(many=False)
    
    prospect = ProspectSmSerializer(many=False)
    
    job_type = JobtypeSerializer(many=False)
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