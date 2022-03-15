from rest_framework import serializers
from CV_ables_api.models import Mission
from CV_ables_api.serializers import ApplicantSmallSerializer, JobtypeSerializer
class MissionSerializer(serializers.ModelSerializer):
    applicant = ApplicantSmallSerializer(many=False)
    
    job_type = JobtypeSerializer(many=False)
    class Meta:
        model = Mission
        fields = (
            'id',
            'mission_text',
            'applicant',
            'job_type'
        )    
class MissionSmSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mission
        fields = (
            'id',
            'mission_text'
        )