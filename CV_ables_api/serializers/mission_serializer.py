from rest_framework import serializers
from CV_ables_api.models import Mission
from CV_ables_api.serializers import ApplicantSmallSerializer, JobtypeSerializer
class MissionSerializer(serializers.ModelSerializer):
    applicant = ApplicantSmallSerializer(many=False)
    
    jobtype = JobtypeSerializer(many=False)
    class Meta:
        model = Mission
        fields = (
            'id',
            'mission_text',
            'applicant',
            'jobtype'
        )    
class MissionSmSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mission
        fields = (
            'id',
            'mission_text'
        )