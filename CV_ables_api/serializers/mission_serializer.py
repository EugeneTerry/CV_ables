from rest_framework import serializers
from CV_ables_api.models import Mission
from CV_ables_api.serializers import ApplicantSerializer, JobtypeSerializer
class MissionSerializer(serializers.ModelSerializer):
    applicant = ApplicantSerializer(many=False)
    
    jobtype = JobtypeSerializer(many=False)
    class Meta:
        model = Mission
        fields = (
            'id',
            'mission_text',
            'applicant',
            'jobtype'
        )